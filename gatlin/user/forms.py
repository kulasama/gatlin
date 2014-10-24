#coding:utf8
from flask.ext.wtf import Form, RecaptchaField

from wtforms import StringField, PasswordField, BooleanField, HiddenField
from wtforms.validators import (DataRequired, Email, EqualTo, regexp,
                                ValidationError)



class SigninForm(Form):
    login = StringField(u"用户名", validators=[
        DataRequired(message=u"用户名")])

    password = PasswordField(u"密码", validators=[
        DataRequired(message="Password required")])

    remember_me = BooleanField("Remember Me", default=False)
