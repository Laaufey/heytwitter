import g
from bottle import post, delete, request, redirect, response

import mysql.connector
import jwt


@delete("/users/<user_id>")
def _(user_id):
    user_session = request.get_cookie("token")
    decoded_session = jwt.decode(
        user_session, "super_secret", algorithms=["HS256"])

    conn = mysql.connector.connect(**g.DB_CONFIG)
    db = conn.cursor(dictionary=True)

    delete_user_query = f"""
        DELETE FROM users 
        WHERE user_id = %(user_id)s
    """

    user = {"user_id": user_id}

    db.execute(delete_user_query, user)

    conn.commit()

    response.status = 200

    return user
