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
        response="CON what would you want to check\n"
        response +="1.your account_number\n"
        response += "2.your phone_number\n"


    elif text=='1':
        response="CON what would you like to check\n"
        response += "1.your account_number\n"
        response += "your account_balance\n"

    elif text == '1*1':
        account_number =" SVCV73HDBH72"
        response="END your account_number is " +account_number

    elif text == '1*2':
        account_balance ="7,405,423,618"
        response="END your phone_number is " +account_balance

    elif text == '2':
        response="END your phone_number is " +phone_number

    return response
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
