import json
from functools import wraps

from flask import abort,redirect,url_for
from flask.ext.login import current_user


def signin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if current_user is not None and current_user.is_authenticated():
            return f(*args, **kwargs)
        else:
            return redirect(url_for("user.signin"))
    return decorated


def signout_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if current_user is not None and current_user.is_authenticated():
            return redirect(url_for("user.profile"))
        return f(*args, **kwargs)
    return decorated

def json_wrap(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        return json.dumps(f(*args,**kwargs))
    return decorated