import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_API_KEY')
service_sid = os.getenv('TWILIO_SYNC_SERVICE_SID')

"""
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_SYNC_SERVICE_SID = os.getenv('TWILIO_SYNC_SERVICE_SID')
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')
TWILIO_API_SECRET = os.getenv('TWILIO_API_SECRET')
"""

client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':
        verification = client.verify \
            .services(service_sid) \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)

        return render_template('otp_verify.html')
    else:
        return "Entered User ID or Password is wrong"

if __name__ == "__main__":
    app.run()
