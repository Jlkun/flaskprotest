# -*- coding: utf-8


#用flask框架来写mock
from flask import Flask,request,json,abort
#123
app=Flask(__name__)

class mymock():
    def __init__(self,**kwargs):
        self._cardNo = kwargs.get('cardNo', "3104830020100299977")
        self._key_index = kwargs.get('keyIndex', '0')

    @app.route("/<path:path>",methods=['GET'])
    def index(path):
        return  "12"

    @app.route("/mock",methods=['GET','POST'])
    def mock(self):
        if request.method == 'GET':
            abort(404)
        else:
            try:
                name=request.form['name']
                print(name)
                if name=='kevin':
                    data={"status": 200, "message": "True", "response": {"orderID": 100}}
                else:
                    data ={"status": 400, "message": "False", "response": {}}
            except:
                data = {"status": 500, "message": "Server Error", "response": {}}
            return json.dumps(data)

    def run(self):
        app.run(host='0.0.0.0')

    def test(self):
        print(123)

if __name__=='__main__':
    app.run(host='0.0.0.0')



