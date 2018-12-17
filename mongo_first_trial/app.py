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


@app.route('/search', methods=['GET'])
def get_all_items():
	docs = [doc for doc in items.find({})]
	print(docs)
	JSONEncoder().encode(docs)
	return jsonify({'docs':JSONEncoder().encode(docs)})
	
@app.route('/search/<string:item>', methods=['GET'])
def get_one_item(item):
	collections = db['transactions']
	docs = [doc for doc in collections.find({},{item:1,'_id':0})]
	
	return Response(json.dumps({'success':True, 'message':docs}))
	
	#docs = [for doc in db.items.find(items:{$elemMatch:{return:item}}})]
	#docs = [doc for doc in items.find({},{"[item]":1,'_id':0})]
	#print(docs)
	#JSONEncoder().encode(docs)
	#return jsonify({"docs":JSONEncoder().encode(docs)})

@app.route('/add', methods=['GET'])
def add():
	user = mongo.db.users
	user.insert()
	return 'Added user!'

if __name__ =="__main__":
	app.run(debug = True)