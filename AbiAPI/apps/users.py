from apistar import annotate, Route
from apistar.authentication import Auth
from pymongo.database import Database
from common.auth.permissions import IsLogin


def ls(mongo: Database):
    return list(mongo.users.distinct('username'))


@annotate(permissions=[IsLogin()])
def current_user(auth: Auth, mongo: Database):
    user = mongo.users.find_one({'username': auth.get_display_name()}, {'_id': 0, 'password': 0})
    return {'code': 200, 'data': user}


user_routes = [
    Route('/ls', 'GET', ls, name='users_ls'),
    Route('/whoami', 'GET', current_user)
]
