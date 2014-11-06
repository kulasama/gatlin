# -*- coding: utf-8 -*-
import json

from flask import Blueprint, current_app, flash, request
from flask import render_template
from flask.ext.login import current_user
from gatlin.user.models import User
from gatlin.network.models import Status,Feed
from gatlin.utils.decorators import signin_required,json_wrap
from datetime import datetime



network = Blueprint("network", __name__, template_folder="templates")



@network.route("/")
@signin_required
def index():
    feeds = Feed.query.order_by(Feed.created.desc()).limit(20)
    return render_template("index.html",feeds=feeds)



@network.route("/status/",methods=["POST"])
@signin_required
@json_wrap
def create_status():
    if request.method == "POST":
        try:
            form = json.loads(str(request.data,encoding = "utf-8"))           
            text = form.get("status")
            status = Status(text=text,author=current_user.id)
            status.save()
            feed = Feed(data=request.data,author=current_user.id,feed_type=Status.FEED_TYPE)
            feed.created = datetime.now()
            feed.save()
            return status.to_dict()
        except:
            import traceback
            traceback.print_exc()
    return {}






 
