import imp
from bottle import get, view, response, request, redirect
import g
import jwt

import mysql.connector


@get("/<user_name>")
@view("profile")
def _(user_name):
    try:
        conn = mysql.connector.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        response.set_header(
            "Cache-Control", "no-cache, no-store, must-revalidate")
        # we don't need to retrieve the user from the db since we have the jwt
        user_session = request.get_cookie("token")
        decoded_session = jwt.decode(
            user_session, "super_secret", algorithms="HS256")
        print("DECODED SESSION")
        print(decoded_session)

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
        user_id = {"user_id": user_profile["user_id"]}
        print("USER PROFILE")
        print(user_profile)
        db.execute(user_profile_tweets_query, user_id)
        tweets = db.fetchall()
        tweets_count = len(tweets)
        print("COUNT "*5)
        print(tweets_count)
        user_name = {"user_name": decoded_session["user_name"]}
        query_users = f"""
            SELECT * FROM users
            WHERE user_name != %(user_name)s
            AND user_name != "admin"
            ORDER BY RAND() LIMIT 3
            """
        db.execute(query_users, user_name)
        user_id = {"user_id": decoded_session["user_id"]}
        users = db.fetchall()
        like_query = f"""
            SELECT * FROM likes
        """
        db.execute(like_query, user_id)
        likes = db.fetchall()

        user_likes = list()
        tweet_counts = dict()
        for like in likes:
            t_id = like["tweet_id"]
            # add tweet id to a list of ids if user has liked the id
            if like["user_id"] == user_id["user_id"]:
                user_likes.append(t_id)

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
        print("USERS TO FOLLOW")
        print(users)
        return dict(tabs=g.tabs, user_likes=user_likes, likes=likes, like_count=like_count, user_profile=user_profile, tweets_count=tweets_count, user=decoded_session, tweets=tweets, trends=g.trends, whoToFollow=g.whoToFollow, users=users)
    except Exception as ex:
        print(ex)
