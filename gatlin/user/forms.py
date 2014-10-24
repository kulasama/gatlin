#coding:utf8
from flask.ext.wtf import Form, RecaptchaField

from wtforms import StringField, PasswordField, BooleanField, HiddenField
from wtforms.validators import (DataRequired, Email, EqualTo, regexp,
                                ValidationError)

from gatlin.user.models import User

from datetime import datetime

class SigninForm(Form):
    login = StringField(u"用户名", validators=[
        DataRequired(message=u"用户名")])

    password = PasswordField(u"密码", validators=[
        DataRequired(message="Password required")])

    remember_me = BooleanField("Remember Me", default=False)

class SignupForm(Form):
    username = StringField(u"用户名",validators=[
        DataRequired(message=u"请填写用户名")])
    email = StringField(u"邮箱",validators=[
        DataRequired(message=u"请填写邮箱")])
    password = PasswordField(u"密码",validators=[
        DataRequired(message=u"请填写密码")])
    password_confirm = PasswordField(u"确认密码",validators=[
        DataRequired(message=u"请填写确认密码"),
        EqualTo("password", message="两次输入密码不一致")])


    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("This username is taken")

    def validate_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if email:
            raise ValidationError("This email is taken")

    def save(self):
        user = User(username=self.username.data,
                    email=self.email.data,
                    password=self.password.data,
                    joined=datetime.utcnow())
        return user.save()

