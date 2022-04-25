from bottle import post, response, redirect, request
import g
import imghdr
import uuid

import mysql.connector
import jwt
import time
import os
from g import TWEET_TEXT_MAX_LENGTH, TWEET_TEXT_MIN_LENGTH


@post("/post_tweet")
def _():
    try:
        ##############################
        # VALIDATE
        # Validate text
        if not request.forms.get("tweet"):
            response.status = 400
            return {"info": "Tweet text is missing"}

        tweet = request.forms.get("tweet").strip()

        if len(tweet) < TWEET_TEXT_MIN_LENGTH:
            response.status = 400
            return {"info": f"Tweet must be at least {TWEET_TEXT_MIN_LENGTH} characters long"}

        if len(tweet) > TWEET_TEXT_MAX_LENGTH:
            response.status = 400
            return {"info": f"Tweet can only have a maximum of {TWEET_TEXT_MAX_LENGTH} characters"}

        # Validate image
        image_name = None

        if request.files.get("tweet_image"):
            tweet_image = request.files.get("tweet_image")
            file_name, file_extension = os.path.splitext(
                tweet_image.filename)  # .png .jpeg .zip .mp4
            print(file_name)
            print(file_extension)

            # Validate extension
            if file_extension not in (".png", ".jpeg", ".jpg", ".gif"):
                response.status = 400
                return {"info": "This image is not allowed"}

            # overwrite jpg to jpeg so imghdr will pass validation
            if file_extension == ".jpg":
                file_extension = ".jpeg"

            image_id = str(uuid.uuid4())
            # Create new image name
            image_name = f"{image_id}{file_extension}"

            # Save the image
            tweet_image.save(f"images/{image_name}")

            # Make sure that the image is actually a valid image
            # by reading its mime type
            imghdr_extension = imghdr.what(f"images/{image_name}")

            if file_extension != f".{imghdr_extension}":
                # remove the invalid image from the folder
                os.remove(f"images/{image_name}")
                response.status = 400
                return {"info": "This image format is not allowed"}

            print("#"*30)
            print(image_name)
        ##############################
        # Connecting to the database

        conn = mysql.connector.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        user_session = request.get_cookie("token")
        decoded_session = jwt.decode(
            user_session, "super_secret", algorithms=["HS256"])

        user_query = f"""
        SELECT * FROM users WHERE user_id = %(user_id)s
        """

        user_id = {"user_id": decoded_session["user_id"]}

        db.execute(user_query, user_id)

        user = db.fetchone()

        ##############################
        # Tweet

        tweet = {
            "tweet_id": str(uuid.uuid4()),
            "user_first_name": user["user_first_name"],
            "user_last_name": user["user_last_name"],
            "user_name": user["user_name"],
            "user_img": user["user_img"],
            "fk_user_id": user["user_id"],
            "tweet_date": time.time(),
            "tweet_text": tweet,
            "tweet_image": image_name
        }

        db.execute("""
        INSERT INTO tweets (tweet_id, user_first_name, user_last_name, user_name, user_img, fk_user_id, tweet_date, tweet_text, tweet_image)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(tweet.values()))

        conn.commit()
        response.status = 201
        # Make sure that the image is actually a valid image
        # by reading its mime type
        return tweet
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info": "Something went wrong"}
