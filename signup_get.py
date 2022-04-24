
from bottle import get, view


@get("/signup")
@view("index")
def _():
    print("SIGNUP_GET")
    return
