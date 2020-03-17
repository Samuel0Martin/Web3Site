from flask import Flask, render_template, redirect
from random import random
from math import floor
from mongoengine import *

app = Flask(__name__)

connect('web3_DB')

class User(Document):
    email = StringField()
    first_name = StringField()
    last_name = StringField()

class Country(Document):
    name = StringField()

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')
	
@app.route('/inspire')
@app.route('/inspiration')
def inspire():
    return render_template('inspiration.html')	

@app.route('/page1')
def hello_world():
	bob = User(email='a123@b123', first_name='Bob', last_name='Bob2').save()
	return 'Hello, World!'

@app.route('/createCountry')
def create_world():
	Country(name='Bobs Country').save()
	return 'Created a new Country'

@app.route('/page2')
def return_world():
	return 'This is the second page.'

@app.route('/page3')
def great_world():
	num = random() * 100
	return 'This is page ' + str(floor(num)) + '.'

@app.route('/page4')
def fourth_world():
	num = random() * 45345645348564853533321323546423097
	return 'This is the page number: ' + str(floor(num))

@app.route('/page5')
def fifth_world():
	return User.objects.to_json()

@app.route('/pageCountry')
def all_world():
	for country in Country.objects:
		print(country.name)
	return Country.objects.to_json()
	
	
@app.route('/countries', methods=['POST'])
def addCountry():
	Country(name='Country A').save()
	return 'Created a new Country'
	
@app.route('/countries', methods=['GET'])
def findCountries():
	countries = Country.objects
	return countries.to_json()
	
@app.route('/countries/<country_id>', methods=['GET'])
def getCountry(country_id=None):
	countries = None
	if country_id is None:
		countries = Country.objects
	else:
		countries = Country.objects.get(id=country_id)
	return countries.to_json()
	
@app.route('/countries', methods=['DELETE'])
def deleteCountry():
	Country.objects.get(name='Country A').delete()
	return 'Removed a Country'


if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=80)