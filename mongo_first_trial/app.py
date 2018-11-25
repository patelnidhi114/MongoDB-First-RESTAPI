from flask import Flask,render_template,jsonify,json,request
import json
import pymongo
import bson;
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongo_first_db'
app.config['MONGO_URI'] = 'mongodb://nidhi:nidhi123@ds119350.mlab.com:19350/mongo_first_db'

mongo = PyMongo(app)

@app.route('/items', methods=['GET'])
def get_all_items():
	items = mongo.db.transactions

	output = []
	for each in items.find():
		output.append(each)
	return jsonify({output})

def add():
	user = mongo.db.users
	user.insert()
	return 'Added user!'

if __name__ == '__main__':
	app.run(debug=True)
