from flask_pymongo import PyMongo

from flask import Flask, jsonify, request

from app import app as app


mongo = PyMongo(app)


@app.route('/users', methods=["GET"])
def get_all_users():
    users_collection = mongo.db.users
    
    results = []

    for user in users_collection .find():
        results.append({'name' : user["name"], 'age' : user["age"]})
    
    return jsonify({'output': results})


@app.route('/users', methods=["GET"])
def get_one_user(name):
    users_collection = mongo.db.users
    
    user = users_collection.find_one({"name": name})

    if user:
        results = ({"name": user["name"], "age": user["age"]})
    else:
        resusts = "User not found"
    
    return jsonify({'output': results})

@app.route('/users', methods=["POST"])
def create_user():
    users_collection = mongo.db.users

    name = request. get_json()["name"]
    age = request. get_json()["age"]

    
    user_id = users_collection.insert({"name": name, "age": age})
    new_user = users_collection.find_one({"_id": user_id})

    results = ({"name": new_user["name"], "age": new_user["age"]})
    
    return jsonify({'output': results})
