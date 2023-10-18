from functools import wraps

from flask import abort

from bisellium.lib.api_clients.exceptions import APIEndpointException


def api_call(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except APIEndpointException as e:
            abort(500, e)
        except:
            abort(500, "Unknown error.")

    return decorated_func
