from bottle import default_app, get, post, run, static_file, view, request
import g
from g import tabs, people, trends, tweets, whoToFollow
import mariadb



##############################
import signup_get      # GET
import signup_ok_get   # GET
import login_get       # GET
import home_get        # GET
import logout_get      # GET
import tweet_get       # GET

import signup_post     # POST
import login_post      # POST
import tweet_post      # POST

##############################
@get("/spa.js")
def _():
  return static_file("spa.js", root=".")

##############################
@get("/")
@view("index")
def _():
  is_xhr = True if request.headers.get('spa') else False
  return dict(title="Index", tabs=tabs, tweets=tweets, trends=trends, whoToFollow=whoToFollow, users=g.USERS, is_xhr=is_xhr)

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")
##############################
@get("/images/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images")
##############################
@get("/app.js")
def _():
  return static_file("app.js", root=".")
##############################
try: 
  import production
  application = default_app()
except Exception as ex:
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
