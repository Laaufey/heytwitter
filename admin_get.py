import re
from bottle import get, view, response, request, redirect
import g

import mysql.connector
import jwt


@get("/admin")
@view("admin")
def _():
    user_session = request.get_cookie("token")
    if not user_session:
        return redirect("/")
    try:
        conn = mysql.connector.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        is_xhr = True if request.headers.get('spa') else False

        response.set_header(
            "Cache-Control", "no-cache, no-store, must-revalidate")
        # we don't need to retrieve the user from the db since we have the jwt

        decoded_session = jwt.decode(
            user_session, "super_secret", algorithms="HS256")

        user_query = f"""
        SELECT * FROM users
        """
        db.execute(user_query)
        users = db.fetchall()

        db.execute("SELECT * FROM tweets ORDER BY tweet_date DESC")
        tweets = db.fetchall()

        conn.commit()
        conn.close()
        return dict(title="Admin", is_xhr=is_xhr, tweets=tweets, users=users, tabs=g.tabs, trends=g.trends, whoToFollow=g.whoToFollow, user=decoded_session)
    except Exception as ex:
        print(ex)
        response.status = 500
    return {"info": "Something went wrong, try again later"}
