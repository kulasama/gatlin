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

def render_json(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        returned = f(*args,**kwargs)
        if isinstance(returned,tuple):
            data = json.dumps(returned[0])
            wrapped = (data,) + returned[1:] 
            return wrapped
        else:
            return json.dumps(returned)
    return decorated