from bson import ObjectId
from bson.json_util import dumps
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

from schemas import UserModel

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/database"
mongo = PyMongo(app)
users_collection = mongo.db.users


@app.route('/users', methods=['GET'])
def get_users():
    users = users_collection.find()
    print(users_collection)
    return dumps(users)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404
    

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.json
    validated_users = UserModel(**user_data).to_mongo() 
    result = users_collection.insert_one(validated_users)
    return jsonify({'message': 'Item added', 'id': str(result.inserted_id)}), 201


@app.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    user_data = request.json
    validated_user = UserModel(**user_data).to_mongo()
    del validated_user["_id"]
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": validated_user})
    if result.did_upsert:
        return jsonify({"message": "User updated"})
    return jsonify({"message": "User not found"}), 404


@app.route('/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
