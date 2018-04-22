from apistar import Route
from common.mongodb import MongoClient


def name(id: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"strategyName": 1})
    resp = {"strategyName": data['strategyName']}
    return resp


def basic_info(id: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"basic": 1, "_id": 0})
    return data['basic']


def net_values(id: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"netValues": 1, "_id": 0})
    return data['netValues']


def style_risks_keys(id: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"styleRisks": 1, "_id": 0})
    return list(data['styleRisks'].keys())


def style_risks(id: str, key: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"styleRisks": 1, "_id": 0})
    return data['styleRisks'][key]


def industry_risks_keys(id: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"industryRisks": 1, "_id": 0})
    return list(data['industryRisks'].keys())

def industry_risks(id: str, key: str, mongo: MongoClient):
    data = mongo.abigale.strategy.find_one({"fileId": id}, {"industryRisks": 1, "_id": 0})
    return data['industryRisks'][key]


detail_routes = [
    Route('/name', 'GET', name),
    Route('/basic', 'GET', basic_info),
    Route('/netValues', 'GET', net_values),
    Route('/styleRisks/keys', 'GET', style_risks_keys),
    Route('/styleRisks/query/{key}', 'GET', style_risks),
    Route('/industryRisks/keys', 'GET', industry_risks_keys),
    Route('/industryRisks/query/{key}', 'GET', industry_risks),
]
