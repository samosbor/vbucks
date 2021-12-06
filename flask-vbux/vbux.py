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
    print(stripe_payload['data']['object']['shipping'])
    if stripe_payload["data"]["object"]['object']=='payment_intent':
        if int(stripe_payload['data']['object']['charges']['total_count']) > 0:
            shipping_address_json = stripe_payload["data"]["object"]["shipping"]["address"]
            #add stripe payload to an email creation engine to send an email when we receive an incoming request
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login('visalden0@gmail.com', 'suppleT1DD13$')
                sent_from = 'visalden0@gmail.com'
                to = ['hallwyatt3@gmail.com',] #add sam.osborne159@gmail.com when done testing
                body = f'Address:\n{shipping_address_json["line1"]}\n{shipping_address_json["line2"]}\n{shipping_address_json["city"]}, {shipping_address_json["state"]}, {shipping_address_json["postal_code"]}\n{shipping_address_json["country"]}'
                email_text = f'From: visalden0@gmail.com\nTo: hallwyatt3@gmail.com, sam.osborne159@gmail.com\nSubject: New Order Received!\n\n{body}'
                server.sendmail(sent_from, to, email_text)
                server.close()
            except:
                print('Something went wrong...')
    return "Hello world"