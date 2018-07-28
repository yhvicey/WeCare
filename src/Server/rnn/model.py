import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import re
import gc

from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, GRU, Embedding
from tensorflow.python.keras.models import load_model

graph = tf.get_default_graph()


def load_rnn_model(modelPath:str):
    model = load_model(modelPath)
    adam_optimizer = tf.train.AdamOptimizer()
    model.compile(optimizer=adam_optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return model

def ParseToken2Index(tokenindexPath:str):
    tokenindexDict = dict()
    
    fileTokenIndex = open(tokenindexPath, 'rt', encoding="utf8")
    lines = fileTokenIndex.readlines()
    
    for line in lines:
        matchObj = re.match(r"^\"(.*?)\";\"(.*?)\"$", line)
        tokenindexDict[matchObj.group(1)] = int(matchObj.group(2))
        
    fileTokenIndex.close()
        
    return tokenindexDict

def GetEmotionIcon(emotionFilePath:str):
    fileEmotionIcon = open(emotionFilePath, 'rt', encoding="utf8")
    iconLines = fileEmotionIcon.readlines()

    icons = list()
    
    for iconLine in iconLines:
        icons.append(re.split(r'\t', iconLine)[0])
        
    fileEmotionIcon.close()
    
    return sorted(icons,key=len,reverse=True)

def GetSymbols(symbolFilePath:str):
    fileSymbols = open(symbolFilePath, 'rt', encoding="utf8")
    symbolLines = fileSymbols.readlines()
    
    symbols = list()
    
    for symbolLine in symbolLines:
        symbol = symbolLine.strip()
        if symbol not in symbols:
            symbols.append(symbol)
    
    fileSymbols.close()
    
    return sorted(symbols, key=len, reverse=True)

def IsStopWord(word):
    if word.startswith('@'):
        return True
    elif re.match(r'(http|https):\/\/[\w\-]+(\.[\w\-]+)+\S*', word):
        return True
    else:
        return False
    
def IsAreaWord(word):
    if word.startswith('#'):
        return True
    else:
        return False
    
def IsPureDigital(word):
    if re.match(r'^[0-9]*$', word):
        return True
    else:
        return False

def TmpTokenize(tmpToken, icons):
    if tmpToken == '':
        return list()
    finalTokenList = list()
    foundIcon = ''
    foundSymbol = ''
    if IsStopWord(tmpToken):
        finalTokenList.append('<StopWord>')
    elif IsPureDigital(tmpToken):
        finalTokenList.append('<PureNum>')
    elif IsAreaWord(tmpToken):
        finalTokenList.append(tmpToken)
    else:
        for icon in icons:
            if icon in tmpToken:
                foundIcon = icon
                break
        if foundIcon != '':
            pos = tmpToken.find(foundIcon)
            if pos == 0:
                finalTokenList.append(tmpToken[0:len(foundIcon)])
                finalTokenList += TmpTokenize(tmpToken[len(foundIcon):], icons)
            else:
                finalTokenList += TmpTokenize(tmpToken[0:pos], icons)
                finalTokenList.append(tmpToken[pos:pos+len(foundIcon)])
                finalTokenList += TmpTokenize(tmpToken[pos+len(foundIcon):], icons)
        else:
            finalTokenList.append(tmpToken)
                
    return finalTokenList

    
def TwitterTokenize(sentence, icons):
    #Deal with Special emotion icons:
    sentence = sentence.replace('(^ ^)', '(^^)')
    sentence = sentence.replace('( ^)o(^ )', '(^)o(^)')
    sentence = sentence.replace('( 一一)', '(一一)')
    sentence = sentence.replace('<(_ _)>', '<(__)>')
    sentence = sentence.replace('>_>^ ^<_', '>_>^^<_')
    sentence = sentence.replace('∩( ・ω・)∩', '∩(・ω・)∩')
    sentence = sentence.replace('( ・ω・)', '(・ω・)')
    sentence = sentence.replace('m(_ _)m', 'm(__)m')
    
    sentence = sentence.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '\"')
    sentence = sentence.lower()
    tokens = list(filter(None, re.split(r' ', sentence)))

    finalTokenList = list()
    finalTokenList.append('<START>')
    
    for token in tokens:
        parsedTokens = TmpTokenize(token, icons)
        for parsedToken in parsedTokens:
            finalTokenList.append(parsedToken)

    finalTokenList.append('<END>')
    
    return finalTokenList


def isIllegalSentence(parsedTokenList:list, meaninglessTokenNum: int, totalTokenNum:int):
    parsedTokenNum = len(parsedTokenList) - 2 - meaninglessTokenNum
    realTokenNum = totalTokenNum - 2
    if float(parsedTokenNum/realTokenNum) < 0.7:
        return True
    else:
        return False
    

def predicateSentenceSentiment_TwoPolarity(model, icons, sentences:list, tokenindexDict:dict, numOfMaxWordPerSentence = 200, paddingWay = 'pre'):
    tokensPredicationList = list()
    predictResultList = list()
    illegalSentenceIndexList = list()
    sentenceIndex = 0
    predicationResultIndex = 0

    for sentence in sentences:
        tokens = TwitterTokenize(sentence, icons)
        parsedTokens = list()
        totalTokenNum = 0
        meaninglessTokenNum = 0
        for token in tokens:
            totalTokenNum += 1
            if token in tokenindexDict:
                if token == '<PureNum>' or token == '<StopWord>':
                    meaninglessTokenNum += 1
                parsedTokens.append(tokenindexDict[token])
        isIllegal = isIllegalSentence(parsedTokens, meaninglessTokenNum, totalTokenNum)
        if isIllegal:
            illegalSentenceIndexList.append(sentenceIndex)
        tokensPredicationList.append(parsedTokens)
        sentenceIndex += 1
    
    dataPredication = pad_sequences(tokensPredicationList, maxlen=numOfMaxWordPerSentence, padding=paddingWay)

    with graph.as_default():
        predictResults = model.predict(dataPredication)
    
    for predictResult in predictResults:
        if predicationResultIndex in illegalSentenceIndexList:
            predictResultList.append(0)
        else:
            pos = np.argmax(predictResult)
            if pos == 0:
                predictResultList.append(1)
            elif pos == 1:
                predictResultList.append(-1)
            else:
                predictResultList(0)
        predicationResultIndex += 1
    
    return predictResultList


class RnnModel(object):
    def __init__(self):
        self.load()

    def load(self):
        #load model
        self.model = load_rnn_model('./rnn/model_twitter_category2_online.h5')
        self.model.summary()

        #load token-index file
        self.tokenindexDict = ParseToken2Index('./rnn/tokenindex_category2_online.txt')

        #load emotion icon file and symbol icon file
        self.emotionIcons = GetEmotionIcon('./rnn/emoticon.txt')
        self.symbolIcons = GetSymbols('./rnn/symbols.txt')
        self.icons = self.emotionIcons + self.symbolIcons

    def predict(self, str):
        sentenceList = list()
        sentenceList.append(str)
        predicationResults = predicateSentenceSentiment_TwoPolarity(self.model, self.icons, sentenceList, self.tokenindexDict)
        return predicationResults[0]
