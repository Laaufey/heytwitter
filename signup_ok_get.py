from bottle import get, request, view
from g import tabs, trends, tweets, whoToFollow


@get("/")  # query string expected with email
@view("index")
def _():
    print("SIGNUP_OK_GET")
    error = request.params.get("error")
    user_email = request.params.get("user_email")
    user_name = request.params.get("user_name")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    return dict(error=error, user_email=user_email, user_name=user_name, user_first_name=user_first_name, user_last_name=user_last_name, tabs=tabs, tweets=tweets, trends=trends, whoToFollow=whoToFollow)
