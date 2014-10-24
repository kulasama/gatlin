from gatlin.user.models import User

def test_user(database):
    user = User(username="kula",email="kulasama@gmail.com")
    user.set_password("123123")
    user.save()
    user,auth = User.authenticate("kula","123123")
    assert auth == True
    assert user.username == "kula"