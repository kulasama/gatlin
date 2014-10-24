from flask import Blueprint, flash, request, redirect, url_for

from gatlin.user.forms import SigninForm
from flask.ext.login import (current_user, login_user, login_required,
                             logout_user, confirm_login, login_fresh)


from gatlin.user.models import User
from flask import render_template

user = Blueprint("user", __name__)


@user.route("/sign_in/")
def sign_in():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for("user.profile"))

    form = SigninForm(request.form)
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                                form.password.data)

        if user and authenticated:
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get("next") or
                            url_for("forum.index"))

        flash(("Wrong username or password"), "danger")
    return render_template("user/sign_in.html", form=form)



@user.route("/sign_up/")
def sign_up():
    return render_template("user/sign_up.html")