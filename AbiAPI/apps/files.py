from apistar import Route, annotate, http
from apistar.authentication import Auth
from common.auth.permissions import IsLogin
from common.mongodb import Database
from uuid import uuid4


# @annotate(permissions=[IsLogin()])
def ls(path: str, mongo: Database):
    files = list(mongo.files.find({"path": path}, {"_id": 0}))
    return {"status": 1, "code": 200, "data": files}


# @annotate(permissions=[IsLogin()])
def mkdir(path: str, name: str, mongo: Database, auth: Auth):
    if mongo.files.find({"path": path, "name": name}).count():
        return {"status": 0, "msg": "The target folder already exists", "code": 500}
    mongo.files.insert_one({
        "path": path,
        "name": name,
        "type": "folder",
        "owner": auth.user.username
    })
    return {"status": 1, "code":200}

# TODO: permissions
# @annotate(permissions=[IsLogin()])
def rm_dir(path: str, name: str, mongo: Database):
    target = mongo.files.find_one({"path": path, "name": name})
    if not target:
        return {"status": 0, "msg": "Target doesn't exist", "code": 500}
    elif target['type'] != "folder":
        return {"status": 0, "msg": "Target is not a folder", "code": 500}
    # Recursive remove
    new_path = f"{path}/{name}"
    for content in ls(new_path, mongo):
        if content['type'] == 'folder':
            rm_dir(content['path'], content['name'])
        else:
            rm_file(content['path'], content['name'])
    mongo.files.remove({"_id": target["_id"]})
    return {"status": 1, "code": 200}


# @annotate(permissions=[IsLogin()])
def rm_file(path: str, name: str, mongo: Database):
    target = mongo.files.find_one({"path": path, "name": name})
    if not target:
        return {"status": 0, "msg": "Target doesn't exist", "code": 500}
    elif target['type'] == "folder":
        return {"status": 0, "msg": "Target is a file", "code": 500}
    else:
        mongo.files.remove({"_id": target["_id"]})
        return {"status": 1, "code": 200}

def new_file(path: str, name: str, data: http.RequestData, mongo: Database, auth: Auth):
    query = {"path": path, "name": name, 'type': 'file'}
    target = mongo.files.find_one(query)
    if target is not None:
        return {"status": 0, "msg": "Target already exists", "code": 500}
    file_id = uuid4()
    data['file_id'] = file_id
    mongo.strategy.insert_one(data)
    query['link'] = file_id
    query['owner'] = auth.get_display_name()
    mongo.files.insert_one(query)
    return {"status": 1, "code": 200}
    

file_routes = [
    Route('/ls', 'GET', ls),
    Route('/new', 'POST', new_file),
    Route('/mkdir', 'POST', mkdir),
    Route('/rm_dir', 'POST', rm_dir),
    Route('/rm_file', 'POST', rm_file)
]
