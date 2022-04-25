from bottle import put, request, response
import mysql.connector
import g


@put("/tweets/<tweet_id>")
def _(tweet_id):

    if not request.forms.get("tweet_text"):
        response.status = 400
        return "tweet text missing"

    tweet_text = request.forms.get("tweet_text", "").strip()

    if len(tweet_text) < 1 or len(tweet_text) > 140:
        response.status = 400
        return "tweet must be between 1 and 140 characters"

    # connect to the db
    try:
        conn = mysql.connector.connect(**g.DB_CONFIG)
        db = conn.cursor(dictionary=True)

        # query
        query_update_tweet = ("""
            UPDATE tweets
            SET tweet_text = %(tweet_text)s
            WHERE tweet_id = %(tweet_id)s
        """)

        tweet_data = {"tweet_id": tweet_id, "tweet_text": tweet_text}

        db.execute(query_update_tweet, tweet_data)
        conn.commit()

        return tweet_text

    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        conn.close()

# def _(tweet_ids):
#     user_session = request.get_cookie("token")

#     decoded_session = jwt.decode(
#         user_session, "super_secret", algorithms=["HS256"])

#     print(decoded_session)

#     # Validate tweet_id
#     if not tweet_id:
#         response.status = 400
#         return {"info": "Tweet ID is missing"}

#     tweet_id = int(tweet_id)

#     if tweet_id < 1:
#         response.status = 400
#         return {"info": "Tweet ID is not a valid ID"}

#     query_set_parts = []
#     query_params = {"tweet_id": tweet_id}

#     # Validate text
#     if not request.forms.get("tweet"):
#         response.status = 400
#         return {"info": "Tweet text is missing"}

#     tweet = request.forms.get("tweet_text").strip()

#     if len(tweet) < TWEET_TEXT_MIN_LENGTH:
#         response.status = 400
#         return {"info": f"Tweet must be at least {TWEET_TEXT_MIN_LENGTH} characters long"}

#     if len(tweet) > TWEET_TEXT_MAX_LENGTH:
#         response.status = 400
#         return {"info": f"Tweet can only have a maximum of {TWEET_TEXT_MAX_LENGTH} characters"}

#     query_set_parts.append("tweet_text = %(tweet)s")
#     query_params["tweet_text"] = tweet

#     # Validate image
#     if request.files.get("tweet_image"):
#         tweet_image = request.files.get("tweet_image")
#         file_name, file_extension = os.path.splitext(
#             tweet_image.filename)  # .png .jpeg .zip .mp4
#         print(file_name)

#         # Validate extension
#         if file_extension not in (".png", ".jpeg", ".jpg", ".gif"):
#             response.status = 400
#             return {"info": "This image is not allowed"}

#         # overwrite jpg to jpeg so imghdr will pass validation
#         if file_extension == ".jpg":
#             file_extension = ".jpeg"

#         image_id = str(uuid.uuid4())
#         # Create new image name
#         image_name = f"{image_id}{file_extension}"

#         # Save the image
#         tweet_image.save(f"images/{image_name}")

#         # Make sure that the image is actually a valid image
#         # by reading its mime type
#         imghdr_extension = imghdr.what(f"images/{image_name}")

#         if file_extension != f".{imghdr_extension}":
#             # remove the invalid image from the folder
#             os.remove(f"images/{image_name}")
#             response.status = 400
#             return {"info": "This image format is not allowed"}

#         query_set_parts.append("tweet_image_file_name = %(tweet_image)s")
#         query_params["tweet_image"] = image_name

#     query_set_parts = ",".join(query_set_parts)

#     ##############################
#     # Connect to the database
#     conn = mariadb.connect(**g.DB_CONFIG)
#     db = conn.cursor(dictionary=True)

#     update_tweet_query = f"""
#     UPDATE tweets
#     SET {query_set_parts}
#     WHERE tweet_id = %(tweet_id)s
#     """

#     db.execute(update_tweet_query, query_params)
#     db.commit()
#     print(query_set_parts)
#     print(query_params)

#     response.status = 200
#     return "Success"
