from bottle import get, view, response, request, redirect
import g
import jwt
import mariadb


@get("/<user_name>")
@view("profile")
def _(user_name, ):
    try:
        conn = mariadb.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        response.set_header(
            "Cache-Control", "no-cache, no-store, must-revalidate")
        # we don't need to retrieve the user from the db since we have the jwt
        user_session = request.get_cookie("token")
        user = jwt.decode(
            user_session, "super_secret", algorithms="HS256")
        print(user)

        user_query = f"""
        SELECT * FROM users WHERE user_name = %(user_name)s
        """
        user_name = {"user_name": user_name}
        db.execute(user_query, user_name)
        user_profile = db.fetchone()

        user_profile_tweets_query = f"""
        SELECT *
        FROM tweets
        WHERE fk_user_id = %(user_id)s
        ORDER BY tweet_date DESC
        """
        user_id = {"user_id": user["user_id"]}
        db.execute(user_profile_tweets_query, user_id)
        tweets = db.fetchall()

        return dict(tabs=g.tabs, user_profile=user_profile, user=user, tweets=tweets, trends=g.trends, whoToFollow=g.whoToFollow, users=g.USERS)
    except Exception as ex:
        print(ex)
