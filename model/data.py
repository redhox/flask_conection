# from flask import Flask
# from flask_pymongo import PyMongo
#
#
# app = Flask(__name__)
#
# mongo1 = PyMongo(app, uri="mongodb://localhost:27017/ecole")
#
#
#
# def lire_posts():
#     posts_collection = mongo1["post"]
#     posts = posts_collection.find({})
#     return list(posts)
#
#
# def get_post(id):
#     posts_collection = mongo1["post"]
#     post = posts_collection.find_one({"id": id})
#     return post


