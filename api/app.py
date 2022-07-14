from requests import request
from flask import Flask, request
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

import json
from info import Info

# from db_conn import conn

app = Flask(__name__)

obj = Info()

@app.route('/')
def getInfo():
    return "Welcom to telephon directory"

@app.route('/user',methods=['POST']) 
def add_info():
    data = json.loads(request.data)
    # Bad request -> If payload is not proper 403
    # Internal server Errr --> 500
    obj.save_info(data)
    return { "status": "created", "id": 1 }, status.HTTP_201_CREATED


if __name__ =="__main__":
    app.run(debug=True)