
from bottle import get, view, request


@get("/signup")
@view("index")
def _():
    error = request.params.get("error")
    user_email = request.params.get("user_email")
    user_name = request.params.get("user_name")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    print("SIGNUP_GET")
    return dict(error=error, user_email=user_email, user_name=user_name, user_first_name=user_first_name, user_last_name=user_last_name)
