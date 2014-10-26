# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, flash, request
from flask import render_template
from flask.ext.login import current_user
from gatlin.user.models import User
from gatlin.utils.decorators import signin_required



network = Blueprint("network", __name__, template_folder="templates")



@network.route("/")
def index():
    return render_template("index.html")




