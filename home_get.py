from bottle import get, view, response, request, redirect
import g

import jwt
import mysql.connector


@get("/home")
@view("home")
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

        db.execute("SELECT * FROM tweets ORDER BY tweet_date DESC")

        tweets = db.fetchall()

        user_id = {"user_id": decoded_session["user_name"]}
        query_users = f"""
            SELECT * FROM users
            WHERE user_id != %(user_id)s
            AND user_name != "admin"
            ORDER BY RAND() LIMIT 3
            """
        db.execute(query_users, user_id)
        users = db.fetchall()

        conn.commit()
        return dict(title="Home", is_xhr=is_xhr, tweets=tweets, tabs=g.tabs, trends=g.trends, whoToFollow=g.whoToFollow, user=decoded_session, users=users)
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info": "Something went wrong, try again later"}
