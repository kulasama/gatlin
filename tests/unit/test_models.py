from gatlin.user.models import User
def test_user(database):
    user = User(username="kula",email="kulasama@gmail.com")
    user.set_password("123123")
    user.save()
    print "hello world"
