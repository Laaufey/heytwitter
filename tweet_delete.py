import g
from bottle import post, delete, request, redirect, response

import mysql.connector
import jwt


@delete("/tweets/<tweet_id>")
def _(tweet_id):
    user_session = request.get_cookie("token")
    decoded_session = jwt.decode(
        user_session, "super_secret", algorithms=["HS256"])
    # print("DECODE "*5)
    # print(decoded_session)
    conn = mysql.connector.connect(**g.DB_CONFIG)
    db = conn.cursor(dictionary=True)

    # Validate
    # tweet_id = int(tweet_id)
    # print("TWEET TWEET TWEET TWEET TWEET ")
    # print(tweet_id)
    delete_tweet_query = f"""
        DELETE FROM tweets 
        WHERE tweet_id = %(tweet_id)s
    """

    tweet = {"tweet_id": tweet_id}

    db.execute(delete_tweet_query, tweet)

    conn.commit()

    # print("######"*5)
    # print(db.rowcount)
    response.status = 200

    # return {"info": "Tweed deleted"}
    return tweet
