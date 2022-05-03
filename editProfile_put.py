from bottle import put, request, response
import mysql.connector
import g
import os
import uuid
import imghdr


@put("/users/<user_id>")
def _(user_id):
    if request.files.get("user_img"):
        user_img = request.files.get("user_img")
        file_name, file_extension = os.path.splitext(
            user_img.filename)  # .png .jpeg .zip .mp4
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
        user_img.save(f"images/{image_name}")

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
# user_img = request.forms.get("user_img")

        # connect to the db
        try:
            conn = mysql.connector.connect(**g.DB_CONFIG)
            db = conn.cursor(dictionary=True)

            # query
            query_update_profile_img = ("""
            UPDATE users
            SET user_img = %(user_img)s
            WHERE user_id = %(user_id)s
        """)
            query_update_tweet_img = ("""
            UPDATE tweets
            SET user_img = %(user_img)s
            WHERE fk_user_id = %(user_id)s
            """)

            user_data = {"user_id": user_id, "user_img": image_name}

            db.execute(query_update_profile_img, user_data)
            db.execute(query_update_tweet_img, user_data)

            conn.commit()

            return user_id

        except Exception as ex:
            print(ex)
            response.status = 500
        finally:
            conn.close()
