import os
import json
import base64
from flask import Flask, request,render_template
from google.cloud import pubsub_v1
import psycopg2
import pandas as pd
credential_path='/home/sivayogan/siva/key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=credential_path
publisher=pubsub_v1.PublisherClient()
topic_path='projects/pricebook-etl-stage/topics/email-marketing'
def publish():
    domain='clients.ngpltd.co.uk'
    summary=request.form.get('summary')
    subject=request.form.get('subject')
    pdf=request.files.get('pdf')
    html=summary.split('\n')
    pdf_encoded_string = base64.b64encode(pdf.read())
    credentials="postgresql://postgres:N8et8bmaKPLjpMDg@35.233.13.109:5432/email-templates"
    df=pd.read_sql("""select * from daily_marketing""",con=credentials)

    for row,columns in enumerate(df.values):
        html_string=render_template('daily_marketing.html',cust_name=columns[2],h=html)

        attributes={'name':columns[2],'mail_id':columns[3],'fromEmail':'Northern Gas and Power <trading@ngpltd.co.uk>','domain':domain,'html':html_string,'pdf':'pdf'}
        data=json.dumps(attributes).encode("utf-8")
        future=publisher.publish(topic_path,data)

    return 'finished'
