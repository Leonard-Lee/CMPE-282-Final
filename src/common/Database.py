import pymongo

class Database(object):
    URI = "mongodb://54.191.90.246:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def delete_many(collection, query):
        return Database.DATABASE[collection].delete_many(query)

    @staticmethod
    def update(collection, where, data):
        Database.DATABASE[collection].update_one(where, {'$set': data})