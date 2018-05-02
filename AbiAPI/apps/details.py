from apistar import Route
from common.mongodb import Database


def name(id: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"strategyName": 1})
    resp = {"code": 200, "data": {"strategyName": data['strategyName']}}
    return resp


def basic_info(id: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"basic": 1, "_id": 0})
    return {'code': 200, 'data': data['basic']}


def net_values(id: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"netValues": 1, "_id": 0})
    return {'code': 200, 'data': data['netValues']}

def factor_yields(id: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"factorYields": 1, "_id": 0})
    return {'code': 200, 'data': data['factorYields']}


def style_risks_keys(id: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"styleRisks": 1, "_id": 0})
    return {'code': 200, 'data': list(data['styleRisks'].keys())}


def style_risks(id: str, key: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"styleRisks": 1, "_id": 0})
    return {'code': 200, 'data': data['styleRisks'][key]}


def industry_risks_keys(id: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"industryRisks": 1, "_id": 0})
    return {'code': 200, 'data': list(data['industryRisks'].keys())}

def industry_risks(id: str, key: str, mongo: Database):
    data = mongo.strategy.find_one({"fileId": id}, {"industryRisks": 1, "_id": 0})
    return {'code': 200, 'data': data['industryRisks'][key]}


detail_routes = [
    Route('/name', 'GET', name),
    Route('/basic', 'GET', basic_info),
    Route('/netValues', 'GET', net_values),
    Route('/factorYields', 'GET', factor_yields),
    Route('/styleRisks/keys', 'GET', style_risks_keys),
    Route('/styleRisks/query/{key}', 'GET', style_risks),
    Route('/industryRisks/keys', 'GET', industry_risks_keys),
    Route('/industryRisks/query/{key}', 'GET', industry_risks),
]
