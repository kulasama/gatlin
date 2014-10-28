# -*- coding: utf-8 -*-
import json

from flask import Blueprint, current_app, flash, request
from flask import render_template
from flask.ext.login import current_user
from gatlin.user.models import User
from gatlin.network.models import Status
from gatlin.utils.decorators import signin_required



network = Blueprint("network", __name__, template_folder="templates")



@network.route("/")
@signin_required
def index():
    return render_template("index.html")



@network.route("/status/",methods=["POST"])
@signin_required
def create_status():
    if request.method == "POST":
        try:
            form = json.loads(request.data)           
            text = form.get("status")
            status = Status(text=text,author=current_user.id)
            status.save()
            feed = Feed(data=request.data,author=current_user.id,feed_type=Status.FEED_TYPE)
            feed.save()
        except:
            import traceback
            traceback.print_exc()
    return "create status success"


@network.route("/statuses",methods=["GET"])
@signin_required
def statuses():
    statuses = Status.all()
    data = []
    for status in statuses:
        data.append(status.to_dict())
    return json.dumps(data)

 
