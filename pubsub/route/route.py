from flask import Flask, Response
from controller import publisher

app = Flask(__name__,template_folder='/home/sivayogan/siva/pubsub/templates')
app.add_url_rule('/send_mail_test',view_func=publisher.publish,methods=['POST'])
