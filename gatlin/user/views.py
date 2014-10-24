from flask import Blueprint, flash, request, redirect, url_for

from gatlin.user.forms import SigninForm,SignupForm
from flask.ext.login import (current_user, login_user, login_required,
                             logout_user, confirm_login, login_fresh)


from gatlin.user.models import User
from gatlin.utils.decorators import signout_required,signin_required
from flask import render_template

user = Blueprint("user", __name__)

@signout_required
@user.route("/signin/")
def signin():
    form = SigninForm(request.form)
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                                form.password.data)

        if user and authenticated:
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get("next") or
                            url_for("forum.index"))

        flash(("Wrong username or password"), "danger")
    return render_template("user/signin.html", form=form)



@signout_required
@user.route("/signup/",methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user = form.save()
        login_user(user)
        flash(("Thanks for registering"), "success")
        return redirect(url_for("user.profile", username=current_user.username))
    return render_template("user/signup.html",form=form)


@signin_required
@user.route("/profile")
def profile():
    return "success"

