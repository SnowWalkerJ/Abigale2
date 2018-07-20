from urllib.parse import quote_plus
from apistar import Component, Settings
from pymongo import MongoClient
from pymongo.database import Database


__mongo = None
def init_mongo(settings: Settings):
    global __mongo
    if __mongo is None:
        mongo_uri = "mongodb://{user}:{password}@{host}".format(
            user=quote_plus(settings['MONGO']['user']),
            password=quote_plus(settings['MONGO']['password']),
            host=settings['MONGO']['host'],
        )
        __mongo = MongoClient(mongo_uri).abigale
    return __mongo

MongoDB = Component(Database, init=init_mongo)
