from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello {name} WOAHHHHHH"


@app.route("/webhook", methods=['POST'])
def webhook():
    stripe_payload = request.json
    print(stripe_payload)
    if stripe_payload['data']['object']['object'] == 'payment_intent':
        #add stripe payload to an email creation engine to send an email when we receive an incoming request
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login('sam.osborne159@gmail.com', 'togekisseeveejolteon')

            sent_from = 'sam.osborne159@gmail.com'
            to = ['hallwyatt3@gmail.com']
            body = f'{stripe_payload}'
            server.sendmail(sent_from, to, body)
            server.close()
        except:
            print('Something went wrong...')
    return "Hello world"