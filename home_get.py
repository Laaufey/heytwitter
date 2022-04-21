from bottle import get, view, response, request, redirect
import g 
import mariadb
import jwt


@get("/home")
@view("home")
def _():
  is_xhr = True if request.headers.get('spa') else False

  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  # we don't need to retrieve the user from the db since we have the jwt
  jwt_encoded = request.get_cookie("token")
  if not jwt_encoded:
    return redirect("/login")
  
  user = jwt.decode(jwt_encoded, "super_secret", algorithms="HS256")

  return dict(title="Home", is_xhr=is_xhr, tabs=g.tabs, tweets=g.tweets, trends=g.trends, whoToFollow=g.whoToFollow, user=user, users=g.USERS)

