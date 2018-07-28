import json
import uuid
from datetime import datetime
from threading import Lock

from afinn import Afinn
from rnn.model import RnnModel
from constant import *

afinn = Afinn(emoticons=True)
rnn = RnnModel()


class SessionHandler(object):
    def __init__(self):
        self.lock = Lock()
        self.data = {}          # {'session_id': [{time, content, score}]}
        self.last_update = {}   # {'session_id': datetime}

    def __str__(self):
        return json.dumps(self.data, indent=2)

    @staticmethod
    def generate_session_id():
        return str(uuid.uuid4())

    def add_message(self, session_id, time, content):
        with self.lock:
            self.__clean_session()
            self.last_update[session_id] = datetime.now()

            if session_id not in self.data:
                self.data[session_id] = []

            direction = rnn.predict(content)
            value = afinn.score(content)

            score = direction * abs(value) if value != 0 else direction
            self.data[session_id] += [{
                'time': time,
                'content': content,
                'score': score
            }]

            return score

    def get_score(self, session_id):
        last_scores = [value['score']
                       for value in self.data[session_id][-WINDOW_SIZE:]]
        n = len(last_scores)
        total = 0
        for i in range(n):
            total += 1.0 * (i + 1) / n * last_scores[i]

        return total

    def get_all_message(self, session_id):
        if session_id in self.data:
            return self.data[session_id]
        else:
            return []

    def __clean_session(self):
        now = datetime.now()
        sessions_to_delete = []
        for session_id in self.last_update.keys():
            update_time = self.last_update[session_id]
            if (now - update_time).total_seconds() > SESSION_TIMEOUT:
                sessions_to_delete.append(session_id)
            elif len(self.data[session_id]) >= MAX_CONVERSATION_LENGTH:
                self.data[session_id] = self.data[session_id][:MAX_CONVERSATION_LENGTH - 1]

        for session_id in sessions_to_delete:
            print("Deleted timeout session: %s." % session_id)
            del self.last_update[session_id]
            del self.data[session_id]
