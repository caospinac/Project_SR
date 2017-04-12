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


def test_post_user_if_email_already_exists():
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
    assert res.status == 409


def test_get_user():
    req, res = app.test_client.get(
        '/user/d705a98f06a040bf9952db941681b3ee',
        data={}
    )
    assert res.status == 200


def test_get_user_if_not_exists():
    req, res = app.test_client.get(
        '/user/1d705a98f06a040bf9952db941681b3ii',
        data={}
    )
    assert res.status == 404


def test_patch_user():
    req, res = app.test_client.patch(
        '/user/d705a98f06a040bf9952db941681b3ee',
        data={
            "firstname": "Perengano",
            "lastname": "Primero",
            "email": "perengano1@test.com",
            "phone": "3333333333",
            "password": "mypassword"
        }
    )
    assert res.status == 200


def test_patch_user_if_not_exists():
    req, res = app.test_client.patch(
        '/user/d705a98f06a040bf9952db941681b3iii',
        data={
            "firstname": "Perengano",
            "lastname": "Primero",
            "email": "perengano1@test.com",
            "phone": "3333333333",
            "password": "mypassword"
        }
    )
    print(res.status)
    assert res.status == 404


if __name__ == '__main__':
    try:
        globals()[sys.argv[1]]()
    except AssertionError as e:
        print("Failed test!")
        exit(1)
    else:
        print("Success test!")
        exit(0)
