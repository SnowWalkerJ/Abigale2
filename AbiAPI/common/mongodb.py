from apistar import Component, Settings
from pymongo import MongoClient


__mongo = None
def init_mongo(settings: Settings):
    global __mongo
    if __mongo is None:
        __mongo = MongoClient(**settings['MONGO'])
    return __mongo

MongoDB = Component(MongoClient, init=init_mongo)
