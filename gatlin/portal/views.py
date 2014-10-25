# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, flash, request
from flask import render_template
from gatlin.user.models import User


portal = Blueprint("portal", __name__, template_folder="templates")



@portal.route("/")
def index():
    return render_template("index.html")
