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
			


@app.route('/page3', methods=['GET'])
def great_world():
$.ajax('/jquery/getdata',   // request url
    {
        success: function (data, status, xhr) {// success callback function
            $('p').append(data);
    }
});


	$.ajax({url: "page3", success: function(result){
      $("#div1").html(result);
    }});
	$(document).ready(function(){
		$('/page3').load();
		var name = "Bob";
		console.log(name);
	});
	
	num = random() * 100
	return 'This is page ' + str(floor(num)) + '.'

var name;
$.get("/page3", function(response){
    name = response.name;
    console.log(name);
});
<div id="div1"><h2>Let jQuery AJAX Change This Text</h2></div>

@app.route('/page4')
def fourth_world():
var circle = svg.selectAll("circle")
  .data(data);

circle.exit().remove();

circle.enter().append("circle")
    .attr("r", 2.5)
  .merge(circle)
    .attr("cx", function(d) { return d.x; })
    .attr("cy", function(d) { return d.y; });
	num = random() * 45345645348564853533321323546423097
	return 'This is the page number: ' + str(floor(num))
	
	
@app.route('/endd')
def endd():
    return render_template('page3.html')

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