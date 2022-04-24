import re
from bottle import get, view, response, request, redirect
import g
import mariadb
import jwt


@get("/admin")
@view("admin")
def _():
    user_session = request.get_cookie("token")
    if not user_session:
        return redirect("/")
    try:
        conn = mariadb.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        is_xhr = True if request.headers.get('spa') else False

        response.set_header(
            "Cache-Control", "no-cache, no-store, must-revalidate")
        # we don't need to retrieve the user from the db since we have the jwt

        decoded_session = jwt.decode(
            user_session, "super_secret", algorithms="HS256")

        db.execute("SELECT * FROM tweets ORDER BY tweet_date DESC")

        tweets = db.fetchall()

        conn.commit()
        conn.close()
        return dict(title="Admin", is_xhr=is_xhr, tweets=tweets, tabs=g.tabs, trends=g.trends, whoToFollow=g.whoToFollow, user=decoded_session, users=g.USERS)
    except Exception as ex:
        print(ex)
        response.status = 500
    return {"info": "Something went wrong, try again later"}
