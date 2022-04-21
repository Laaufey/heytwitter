from bottle import get, request, view
from g import tabs, people, trends, tweets, whoToFollow

@get("/index") # query string expected with email
@view("index")

def _():
    user_email = request.params.get("user-email")
    user_name = request.params.get("user-name")
    user_last_name = request.params.get("user-last-name")
    return dict(user_email = user_email, user_name = user_name, user_last_name = user_last_name, tabs=tabs, tweets=tweets, trends=trends, whoToFollow=whoToFollow)