from bottle import delete, request, response
import mysql.connector
import jwt
import g


@delete("/tweets/<tweet_id>/unlike")
def _(tweet_id):
    try:
        conn = mysql.connector.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        user_session = request.get_cookie("token")
        decoded_session = jwt.decode(
            user_session, "super_secret", algorithms=["HS256"])
        print("HELLO")
        # Finding who is liking
        user_query = f"""
        SELECT * FROM users WHERE user_id = %(user_id)s
        """

        user_id = {"user_id": decoded_session["user_id"]}

        db.execute(user_query, user_id)

        user = db.fetchone()

        # Findin which tweet
        tweet_query = f"""
        SELECT * FROM tweets WHERE tweet_id = %(tweet_id)s
        """
        tweet_id = {"tweet_id": tweet_id}
        db.execute(tweet_query, tweet_id)

        tweet = db.fetchone()
        print("#"*30)
        print(tweet)
        # Creating the like and adding it to the likes table

        like = {
            "tweet_id": tweet["tweet_id"],
            "user_id": user["user_id"]
        }

        unlike_query = f"""
          DELETE FROM likes 
          WHERE tweet_id = %(tweet_id)s AND user_id = %(user_id)s
        """

        db.execute(unlike_query, like)

        conn.commit()

        return tweet_id
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info": "Something went wrong"}
