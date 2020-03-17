from flask import Flask, render_template
from random import random
from math import floor

app = Flask(__name__)



@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/inspire')
@app.route('/inspiration')
def inspire():
    return render_template('inspiration.html')



@app.route('/page2')
def return_world():
    return 'This is the second page.'

@app.route('/page3')
def great_world():
	num = random() * 765367389534659346983867439867483768473986723076246720750917095710752379864370984730687067026797208601
	return 'This is page ' + str(floor(num)) + '.'

@app.route('/page4')
def fourth_world():
	num = random() * 45345645348564853533321323545656989907086421414343567680709653453463546788969756434547657097954421324467609097966423
	return 'This is the ' + str(floor(num))


if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=80)