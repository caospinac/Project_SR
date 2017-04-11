import sys

from app import app


def test_post_user():
    req, res = app.test_client.post(
        '/user',
        data={
            "firstname": "paco",
            "lastname": "páez",
            "email": "paco-paez@test.com",
            "phone": "3333333333",
            "password": "mypassword"
        }
    )
    assert res.status == 201


def test_get_user():
    req, res = app.test_client.get(
        '/user/1',
        data={}
    )
    assert res.status == 200


def test_patch_user():
    req, res = app.test_client.get(
        '/user/1',
        data={
            "firstname": "paco",
            "lastname": "páez",
            "email": "paco-paez@test.com",
            "phone": "3333333333",
            "password": "mypassword"
        }
    )
    assert res.status == 200


if __name__ == '__main__':
    globals()[sys.argv[1]]()
