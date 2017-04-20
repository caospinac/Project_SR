import sys

from config import (
    DB_TEST_CLIENT, DB_TEST_NAME,
    SQL_DEBUG
)
from app import app, orm, engine


def test_post_user():
    req, res = app.test_client.post(
        '/user',
        data={
            "firstname": "name",
            "lastname": "lastname",
            "email": "email@test.com",
            "phone": "3333333333",
            "password": "test-password"
        }
    )
    print("Status: ", res.status)
    assert res.status == 201


def test_post_user_if_email_already_exists():
    req, res = app.test_client.post(
        '/user',
        data={
            "firstname": "name2",
            "lastname": "lastname2",
            "email": "email@test.com",
            "phone": "3333333334",
            "password": "test-password2"
        }
    )
    print("Status: ", res.status)
    assert res.status == 409


def test_get_user():
    req, res = app.test_client.get(
        '/user/93df0c3826864c82b15bec51900d9e3a',
        data={}
    )
    print("Status: ", res.status)
    assert res.status == 200


def test_get_user_if_not_exists():
    req, res = app.test_client.get(
        '/user/d705a98notchange9952db941681b3ee',
        data={}
    )
    print("Status: ", res.status)
    assert res.status == 404


def test_patch_user():
    req, res = app.test_client.patch(
        '/user/93df0c3826864c82b15bec51900d9e3a',
        data={
            "firstname": "newname",
            "lastname": "newlastname",
            "email": "new-email@test.com",
            "phone": "3333888334",
            "password": "new-password2"
        }
    )
    print("Status: ", res.status)
    assert res.status == 200


def test_patch_user_if_not_exists():
    req, res = app.test_client.patch(
        '/user/d705a98f06a040bf9952db941681b3iii',
        data={
            "firstname": "newname",
            "lastname": "newlastname",
            "email": "new-email@test.com",
            "phone": "3333888334",
            "password": "new-password2"
        }
    )
    print("Status: ", res.status)
    assert res.status == 404


if __name__ == '__main__':
    test = globals()[sys.argv[1]]
    orm.sql_debug(SQL_DEBUG)
    try:
        engine.bind(DB_TEST_CLIENT, DB_TEST_NAME, create_db=True)
    except Exception as e:
        pass
    else:
        engine.generate_mapping(create_tables=True)

    try:
        test()
    except AssertionError as e:
        print("Failed test!")
        exit(1)
    else:
        print("Success test!")
        exit(0)
