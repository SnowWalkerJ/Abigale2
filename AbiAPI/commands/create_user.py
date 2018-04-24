import re
import getpass
from hashlib import sha256
from apistar.interfaces import Console
from common.mongodb import Database


VALID_PATTERN = r"[A-Za-z][A-Za-z0-9]{5,}"
def create_user(mongo: Database, console: Console, username: str=None, password: str=None):
    """
    Create a new user
    """
    if not username:
        username = input("Username:")
    if not re.fullmatch(VALID_PATTERN, username):
        raise ValueError(f"Username `{username}` not match pattern `{VALID_PATTERN}`")
    if password is None:
        password = getpass.getpass("Password:")
    password = sha256(password.encode()).hexdigest()
    is_admin = input("IsAdmin?(y/[N])")
    is_admin = is_admin in "yY"
    user = mongo.users.find_one({"username": username})
    if user:
        console.echo(f"User `{username}` already exists!")
    else:
        mongo.users.insert({
            "username": username,
            "password": password,
            "isAdmin": is_admin,
        })
        console.echo(f"User `{username}` added.")