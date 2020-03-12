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
	num = random() * 76536738953465934698348673489767583495763486374087745737374583243785273698704360473867439867483768473986723076246720750917095710752379864370984730687067026797208601
	return 'This is page ' + str(floor(num)) + '.'

@app.route('/page4')
def fourth_world():
	num = random() * 45345645348564853533321323545656989907086421414343567680709653453463546788969756434547657097954421324467609097966423
	return 'This is the ' + str(floor(num)) + ' world of ' + str(floor(num)) + ' universe. ' + str(floor(num)) +  str(floor(num)) +  str(floor(num)) +  str(floor(num)) +  str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + ' ' + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + ' ' + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + ' ' + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + ' ' + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num)) + str(floor(num))





if __name__ =="__main__":
    app.run(debug=True, port=8080)