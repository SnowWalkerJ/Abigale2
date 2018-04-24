from apistar.authentication import Auth, Authenticated
from apistar.http import Session, Header, QueryParam, Header
from common.mongodb import Database
from .users import User


class SessionAuthentication:
    def authenticate(self, session: Session):
        print(session.data)
        if 'username' in session:
            username = session['username']
            is_admin = session['isAdmin']
            return Authenticated(username, user=User(username, is_admin))


class BasicAuthentication:
    def authenticate(self, authorization: Header, mongo: Database):
        if authorization is None:
            return None
        scheme, token = authorization.split()
        if scheme.lower() != 'basic':
            return None
        token = base64.b64decode(token).decode("utf-8")
        username, password = token.split(":")
        user = mongo.users.find_one({"username": username, "password": password})
        if user is not None:
            username = user['username']
            is_admin = user['isAdmin']
            return Authenticated(username, user=User(username, is_admin))


class TokenAuthentication:
    def authenticate(self, authorization: Header):
        if authorization is None:
            return None
        scheme, token = authorization.split()
        if scheme.lower() != 'token':
            return None
        if token == 'Abigale@123$':
            return Authenticated('admin', user=User('admin', True))

