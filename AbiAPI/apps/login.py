from apistar.http import RequestData, Session
from apistar import annotate
from apistar.renderers import JSONRenderer
from common.mongodb import Database


@annotate(renderers=[JSONRenderer()])
def login(data: RequestData, mongo: Database, session: Session):
    username = data.get('username')
    password = data.get('password')
    user = mongo.users.find_one({
        'username': username,
        'password': password
    })
    if user is None:
        return {
            'status': 0,
            'code': 300,
            'msg': '用户名/密码不正确'
        }
    else:
        session['username'] = user['username']
        session['isAdmin'] = user['isAdmin']
        return {
            'status': 1,
            'code': 200,
            'username': user['username'],
            'isAdmin': user['isAdmin']
        }


@annotate(renderers=[JSONRenderer()])
def logout(session: Session):
    try:
        del session['username']
        del session['isAdmin']
    except KeyError:
        pass
    return {"status": 1}
