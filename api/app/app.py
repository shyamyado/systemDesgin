from urllib import response
from requests import request
from flask import Flask, request
from flask_api import status

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

    res = -1
    try:
        if data == None or "items"  not in data or len(data['items']) == 0:
            return {"status":"invalid_json"}, status.HTTP_400_BAD_REQUEST

        # Internal server Errr --> 500
        res = obj.save_info(data)
    except:
        return {"status":"internal error"}, status.HTTP_500_INTERNAL_SERVER_ERROR

    return { "status": "created", "id": res }, status.HTTP_201_CREATED

@app.route('/user',methods=["GET"])
def get_user():
    users = obj.get_all_user()
    # users = json.dump(users)
    res = []
    for item in users:
        print("==================")
        print(item)
        user_obj = {}
        user_obj["name"] = item[0]
        user_obj["phone"] = item[1]
        res.append(user_obj)
    
    res = {"items" : res}
    res = json.dumps(res)

    return  res, status.HTTP_200_OK

@app.route('/user/<string:phone>',methods=["GET"])
def get_user_by_phone(phone):
    user = obj.get_user_by_phone(phone)
    if user is None or len(user) == 0 :
        return {"info": "not found"}, status.HTTP_404_NOT_FOUND
    print("=======================")
    print(user)
    res = {"name":user[0],"phone":user[1]}
    res = json.dumps(res)
    return res, status.HTTP_200_OK

@app.route('/user/<string:phone>',methods=["PUT"])
def update_user_details(phone):
    data = json.loads(request.data)
    obj.update_user_details(phone,data)
    return {'updated':data}, status.HTTP_204_NO_CONTENT


if __name__ =="__main__":
   app.run(host='0.0.0.0', port=8082)