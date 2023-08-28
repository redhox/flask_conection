from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

class MongoAccess : 
    __USER = os.getenv('USER_BDD')
    __PW = os.getenv('PASSWORD')
    __HOST = os.getenv('HOST')
    __PORT = os.getenv('PORT')
    __DB_NAME = os.getenv('BDD')
    __COLLECTION_NAME = os.getenv('COLLECTION')

    @classmethod
    def connexion(cls) :
        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@{cls.__HOST}:{cls.__PORT}")
        cls.db = cls.client[cls.__DB_NAME]
        cls.collection = cls.db[cls.__COLLECTION_NAME]
    @classmethod
    def deconnexion(cls) :
        cls.client.close()





    @classmethod
    def get_element(cls, login,passwd):
        cls.connexion()
        user = cls.collection.find_one({'name': login, 'password': passwd})
        cls.deconnexion()
        return user

    @classmethod
    def get_elements(cls):
        cls.connexion()
        tous = cls.collection.find()
        cls.deconnexion()
        return list(tous)

    @classmethod
    def set_element(cls, login, passwd):
        cls.connexion()
        cls.collection.insert_one({'name': login, 'password': passwd})
        cls.deconnexion()