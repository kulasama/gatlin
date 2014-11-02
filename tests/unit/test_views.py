import json

def test_signin(client):
    r = client.get("/user/signin/")
    assert r.status_code == 200



def test_signup(client):
    r = client.get("/user/signup/")
    assert r.status_code == 200

def test_signup_logic(client,database):
    payload = {
        "username":u"kula",
        "password":u"123123",
        "email":u"kulasama@gmail.com",
        "password_confirm":u"123123",
    }
    r = client.post("/user/signup/",data=payload)
    assert r.status_code == 302


