from flask import Flask, render_template, redirect
from random import random
from math import floor
from mongoengine import *
import os
import csv
import json

app = Flask(__name__)

app.config.from_object('config')

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
	dataList = []
	for file in os.listdir(app.config['FILES_FOLDER']):
		filename = os.fsdecode(file)
		path = os.path.join(app.config['FILES_FOLDER'],filename)
		f = open(path)
		r = csv.reader(f)
		d = list(r)
		dataList.append(d)
	return json.dumps(dataList)
			
@app.route('/database')
def db_world():
	for file in os.listdir(app.config['FILES_FOLDER']):
		filename = os.fsdecode(file)
		path = os.path.join(app.config['FILES_FOLDER'],filename)
		f = open(path)
		r = csv.DictReader(f) 
		d = list(r)
		for data in d:
			country = Country()
			dict = {}
			for key in data:
				#print(key:data[key])
				if key == "country":
					#print("123")
					#print(data[key])
					if Country.objects.get(name=data[key]):
					#if Country(name=data[key]).find():
					#if country in Country():
						print(data[key], " already exists")
						# if the country already exists, replace the blank country with the existing country from the db, and replace the blank dict with the current country's data
						#print(data)
					else:
						# if the country does not exist, we can use the new blank country we created above, and set the name
						Country(name=data[key]).add()
						#print(data)
				else:
					f = filename.replace(".csv","")
					if f in dict:
						dict[f][key] = data[key]
					else:
						dict[f] = {key:data[key]}
				# add the data dict to the country
			# save the country
			Country().save()
					
	return 'Created a new Country'

@app.route('/page3')
def great_world():	
	num = random() * 100
	return 'This is page ' + str(floor(num)) + '.'


@app.route('/page4')
def fourth_world():
	num = random() * 45345645348564853533321323546423097
	return 'This is the page number: ' + str(floor(num))
	
	
@app.route('/endd')
def endd():
    return render_template('Page3.html'), 200
	
@app.route('/pageD3')
def d3_js():
    return render_template('PageD3.html')
	
@app.route('/D3Data', methods=['GET'])
def d3_data():
	countries = Country.objects
	return render_template('D3Data.html'), Country.objects.to_json()

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
	
@app.route('/countries/<country_name>', methods=['GET'])
def getCountry(country_name=None):
	countries = None
	if country_name is None:
		countries = Country.objects
	else:
		countries = Country.objects.get(id=country_name)
	return countries.to_json()
	
@app.route('/countries', methods=['DELETE'])
def deleteCountry():
	Country.objects.get(name='Country A').delete()
	return 'Removed a Country'


if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=80)