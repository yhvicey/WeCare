import json
from os import path
from twilio.rest import Client

from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS

from helper import SessionHandler, afinn, rnn
from constant import ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER

app = Flask(__name__)
CORS(app)
sessions = SessionHandler()
twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.route('/', methods=['GET'])
def home():
    return send_file('view/index.html')


@app.route('/query/rnn', methods=['POST'])
def query():
    text = request.get_data().decode()
    print("Calculating direction for \"%s\"" % text)
    return str(rnn.predict(text))


@app.route('/query/afinn', methods=['POST'])
def query_afinn():
    text = request.get_data().decode()
    print("Calculating score for \"%s\"" % text)
    return str(afinn.score(text))


@app.route('/debug/session', methods=['GET'])
def sessions_debug():
    return "<pre>%s</pre>" % str(sessions)


@app.route('/session', methods=['GET'])
def get_session_id():
    return sessions.generate_session_id()


@app.route('/session/<session_id>', methods=['GET', 'POST'])
def message(session_id):
    print("session_id: %s" % session_id)
    if request.method == "GET":
        result = json.dumps(sessions.get_all_message(session_id))
        return result
    elif request.method == "POST":
        try:
            time = request.json['time']
            content = request.json['content']
            return str(sessions.add_message(session_id, time, content))
        except Exception as ex:
            print("Error occurred: %s" % str(ex))
            return "", 500


@app.route('/session/<session_id>/score', methods=['GET'])
def get_session_score(session_id):
    return str(sessions.get_score(session_id))


@app.route('/<path:req_path>', methods=['GET'])
def serve_static_file(req_path):
    file_path = path.join('view', req_path)
    if not path.isfile(file_path) or not path.exists(file_path):
        return "", 404
    return send_from_directory('view', req_path)


@app.route('/action/sms', methods=['POST'])
def send_sms():
    try:
        body = request.json['body']
        to = request.json['to']
        twilio_client.messages.create(
            from_=FROM_NUMBER,
            body=body,
            to=to
        )
        return "true"
    except Exception as ex:
        print("Send SMS failed with error: %s." % str(ex))
        return "false", 400


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
