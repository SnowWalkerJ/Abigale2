from apistar import Component, Settings
from pymongo import MongoClient
from pymongo.database import Database


__mongo = None
def init_mongo(settings: Settings):
    global __mongo
    if __mongo is None:
        __mongo = MongoClient(**settings['MONGO']).abigale
    return __mongo

MongoDB = Component(Database, init=init_mongo)
