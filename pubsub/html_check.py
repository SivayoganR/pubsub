from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/html',methods=['POST'])
def process():
    html=request.form.get('html')
    h_c=html.split('\n')
    html_string=render_template('daily_marketing.html',cust_name='sivayogan',h=h_c)
    print(html_string)
    return 'html'

# app.add_url_rule(process,'/send_mail_test',methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)