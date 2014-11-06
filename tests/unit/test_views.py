#coding:utf8
import json

from gatlin.user.models import User

def test_signin(client):
    r = client.get("/user/signin/")
    assert r.status_code == 200



def test_signup(client):
    r = client.get("/user/signup/")
    assert r.status_code == 200

def test_signup_logic(client,database):
    payload = {
        "username":"kula",
        "password":"123123",
        "email":"kulasama@gmail.com",
        "password_confirm":"123123",
    }
    r = client.post("/user/signup/",data=payload)
    assert r.status_code == 302


def test_signin_logic(client,database):
    user = User(username="kula",email="kulasama@gmail.com")
    user.set_password("123123")
    user.save()
    payload = {
        "login":"kula",
        "password":"123123"
    }
    r = client.post("/user/signin/",data=payload)
    assert r.status_code ==302

def test_create_status(client,database):
    user = User(username="kula",email="kulasama@gmail.com")
    user.set_password("123123")
    user.save()
    payload = {
        "login":"kula",
        "password":"123123"
    }
    r = client.post("/user/signin/",data=payload)
    assert r.status_code ==302

    payload = {
        "status":"test"
    }
    r = client.post("/network/status/",data=payload)
    print (r.status_code)


