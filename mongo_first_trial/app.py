from flask import Flask,render_template,jsonify,json,request,Response
import json
import pymongo
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

auth = HTTPBasicAuth()
uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(uri)
db = client['mongo_first_db']
items = db['transactions']

@auth.get_password
def get_password(username):
	if username == 'nidhi':
		return 'nidhi123'
	return None
	
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

@app.route('/search', methods=['GET'])
def get_all_items():
	docs = [doc for doc in items.find({})]
	print(docs)
	JSONEncoder().encode(docs)
	return jsonify({'aline':JSONEncoder().encode(docs)})
	
@app.route('/search/<item1>', methods=['GET'])
def get_one_item(item1):
	collections = db['transactions']
	docs = collections.find()[0]
	result = docs[item1]
	print(result)
	return Response(json.dumps(result, default=set_default))
	
@app.route('/add', methods=['GET'])
def add():
	user = mongo.db.users
	user.insert()
	return 'Added user!'

if __name__ =="__main__":
	app.run(debug = True)
