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

        user = jwt.decode(
            user_session, "super_secret", algorithms="HS256")

        db.execute("SELECT * FROM tweets ORDER BY tweet_date DESC")

        tweets = db.fetchall()

        # user_name = {"user_name": user["user_name"]}
        user_id = {"user_id": user["user_id"]}
        query_users = f"""
            SELECT * FROM users
            WHERE user_id != %(user_id)s
            AND user_name != "admin"
            ORDER BY RAND() LIMIT 3
            """
        db.execute(query_users, user_id)
        users = db.fetchall()

        like_query = f"""
            SELECT * FROM likes
        """
        db.execute(like_query)
        likes = db.fetchall()

        user_likes = list()
        tweet_counts = dict()
        for like in likes:
            t_id = like["tweet_id"]
            # add tweet id to a list of ids if user has liked the id
            if like["user_id"] == user["user_id"]:
                user_likes.append(t_id)
                print("#"*30)
                print(user_likes)

            # counting the number of tweet_id instances
            if t_id in tweet_counts:
                tweet_counts[t_id] = tweet_counts[t_id] + 1
            else:
                tweet_counts[t_id] = 1

        # add the tweet count to the tweets dictionary
        for tweet in tweets:
            if tweet["tweet_id"] in tweet_counts:
                tweet["count"] = tweet_counts[tweet["tweet_id"]]
            else:
                tweet["count"] = 0

        like_count = len(likes)

        conn.commit()
        return dict(title="Home", user_likes=user_likes, is_xhr=is_xhr, likes=likes, like_count=like_count, tweets=tweets, tabs=g.tabs, trends=g.trends, whoToFollow=g.whoToFollow, user=user, users=users)
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info": "Something went wrong, try again later"}
