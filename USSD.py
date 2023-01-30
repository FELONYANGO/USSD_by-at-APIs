from flask import Flask,request
import os
app = Flask(__name__)

response = ""
@app.route("/",methods=['POST','GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("0740543618", None)
    text = request.values.get("text", "default")


    if text=='':
        response="CON welcome to farmersLine\n"
        response +="1.Enquire about crop\n"
        response += "2.Know more\n"


    elif text=='1':
        
        response = "CON 1.Name your crop\n"
        response += "0.Back\n"
        response += "00.Home\n"

    elif text == '1*1':
        response = "CON 1.Name your area of crop location\n"
        response += "0.Back\n"
        response += "00.Home\n"

    elif text == '1*2':
        account_balance ="7,405,423,618"
        response="END your phone_number is " +account_balance

    elif text == '2':
        response="END your phone_number is " +phone_number

    return response
if __name__ == '__main__':
    app.run(host="0.0.0.0", port='3000')


def connect():
    