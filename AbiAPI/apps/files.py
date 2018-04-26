import json
from apistar import Route, annotate, http, Response
from apistar.renderers import JSONRenderer
from apistar.authentication import Auth
from common.auth.permissions import IsLogin
from common.mongodb import Database
from uuid import uuid4


@annotate(permissions=[IsLogin()])
def ls(path: str, mongo: Database):
    files = list(mongo.files.find({"path": path}, {"_id": 0}))
    return {"status": 1, "code": 200, "data": files}


@annotate(permissions=[IsLogin()])
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


@annotate(permissions=[IsLogin()])
def rm_dir(path: str, name: str, mongo: Database, auth: Auth):
    target = mongo.files.find_one({"path": path, "name": name})
    if not target:
        return {"status": 0, "msg": "Target doesn't exist", "code": 500}
    elif target['type'] != "folder":
        return {"status": 0, "msg": "Target is not a folder", "code": 500}
    if target['owner'] != auth.get_display_name() and not auth.user.is_admin:
        return {"status": 0, "msg": "You can't delete other people's file."}
    # Recursive remove
    new_path = f"{path}/{name}"
    for content in ls(new_path, mongo):
        if content['type'] == 'folder':
            rm_dir(content['path'], content['name'])
        else:
            rm_file(content['path'], content['name'])
    mongo.files.remove({"_id": target["_id"]})
    return {"status": 1, "code": 200}


@annotate(permissions=[IsLogin()])
def rm_file(path: str, name: str, mongo: Database, auth: Auth):
    target = mongo.files.find_one({"path": path, "name": name})
    if not target:
        return {"status": 0, "msg": "Target doesn't exist", "code": 500}
    elif target['type'] == "folder":
        return {"status": 0, "msg": "Target is a file", "code": 500}
    if target['owner'] != auth.get_display_name() and not auth.user.is_admin:
        return {"status": 0, "msg": "You can't delete other people's file."}
    else:
        if "link" in target:
            mongo.strategy.remove({"fileId": target['link']})
        mongo.files.remove({"_id": target["_id"]})
        return {"status": 1, "code": 200}


@annotate(permissions=[IsLogin()])
def new_file_api(path: str, name: str, data: http.RequestData, mongo: Database, auth: Auth):
    query = {"path": path, "name": name}
    target = mongo.files.find_one(query)
    if target is not None:
        return {"status": 0, "msg": "Target already exists", "code": 500}
    file_id = uuid4().hex
    data['file_id'] = file_id
    mongo.strategy.insert_one(data)
    query['link'] = file_id
    query['type'] = 'file'
    query['owner'] = auth.get_display_name()
    mongo.files.insert_one(query)
    return {"status": 1, "code": 200}


@annotate(renderers=[JSONRenderer()], permissions=[IsLogin()])
def new_file_web(body: http.Body, mongo: Database):
    body = body.split(b"\r\n")[4:]
    data = []
    for block in body:
        if block.startswith(b"------WebKitFormBoundary"):
            break
        else:
            data.append(block)
    data = b"\r\n".join(data)
    try:
        data = json.loads(data.decode("utf-8"))
    except json.JSONDecodeError:
        return {"status": 0, "code": 500, "msg": "Not valid json format"}
    file_id = uuid4().hex
    data['fileId'] = file_id
    mongo.strategy.insert_one(data)
    return {"status": 1, "code": 200, "fileId": file_id}


@annotate(permissions=[IsLogin()])
def new_confirm(path: str, name: str, id: str, data: http.RequestData, mongo: Database, auth: Auth):
    query = {"path": path, "name": name}
    target = mongo.files.find_one(query)
    if target is not None:
        return {"status": 0, "msg": "Target already exists", "code": 500}
    query['link'] = id
    query['type'] = 'file'
    query['owner'] = auth.get_display_name()
    mongo.files.insert_one(query)
    return {"status": 1, "code": 200}
    

file_routes = [
    Route('/ls', 'GET', ls),
    Route('/new/api', 'POST', new_file_api),
    Route('/new/web', 'POST', new_file_web),
    Route('/new/confirm', 'POST', new_confirm),
    Route('/mkdir', 'POST', mkdir),
    Route('/rm_dir', 'POST', rm_dir),
    Route('/rm_file', 'POST', rm_file)
]
