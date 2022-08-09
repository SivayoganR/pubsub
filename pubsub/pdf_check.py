import base64
from flask import Flask,request,render_template

app=Flask(__name__)
@app.route('/pdf',methods=['POST'])
def process():
    pdf_file=request.files.get('pdf')
    encoded_string = base64.b64encode(pdf_file.read())
    file_64_decode = base64.b64decode(encoded_string) 
    file_result = open('/home/sivayogan/siva/pubsub/sample_decoded.pdf', 'wb') 
    file_result.write(file_64_decode)
    return 'pdf'

if __name__ == '__main__':
    app.run(debug=True)