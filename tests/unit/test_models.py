from gatlin.user.models import User
from gatlin.network.models import Feed,Status
import json

def test_user(database):
    user = User(username="kula",email="kulasama@gmail.com")
    user.set_password("123123")
    user.save()
    user,auth = User.authenticate("kula","123123")
    assert auth == True
    assert user.username == "kula"


def test_status(database):
    user = User(username="kula",email="kulasama@gmail.com")
    user.set_password("123123")
    user.save()

    status = Status(text="hello world",author=1)
    status.save()
    assert status.to_dict() == {'username': u'kula', 'text': u'hello world', 'author': 1}


def test_feed(database):
    feed = Feed(data=json.dumps({"test":"hello"}),author=1,feed_type=Status.FEED_TYPE)
    feed.save()
