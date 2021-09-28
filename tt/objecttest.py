# -*- coding: utf-8
from flask import Flask,request,json,abort

#用flask框架来写mock
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "hello word"

@app.route("/mock", methods=['GET', 'POST'])
def mock():
    if request.method == 'GET':
        abort(404)
    else:
        try:
            name = request.form['name']
            print(name)
            if name == 'kevin':
                data = {"status": 200, "message": "True", "response": {"orderID": 100}}
            else:
                data = {"status": 400, "message": "False", "response": {}}
        except:
            data = {"status": 500, "message": "Server Error", "response": {}}
        return json.dumps(data)

def run():
    app.run(host='0.0.0.0')


if __name__=='__main__':
    app.run(host='0.0.0.0')

