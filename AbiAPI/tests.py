from apistar.test import TestClient
from apistar.http import Session
from app import app


def test_session():
    from hashlib import sha256
    client = TestClient(app)
    password = sha256('lovefei921'.encode()).hexdigest()
    response = client.post('http://localhost/api/login', data={'username': 'snowwalkerj', 'password': password})
    assert response.json() == {'status': 1, 'username': 'snowwalkerj', 'isAdmin': True}
    whoami = client.get('http://localhost/api/users/whoami')
    assert whoami.json() == {'username': 'snowwalkerj', 'isAdmin': True}

