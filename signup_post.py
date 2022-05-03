from bottle import post, redirect, request, response
import g
import jwt
import uuid

import re
import mysql.connector
from g import (USER_FIRST_NAME_MAX_LENGTH, USER_FIRST_NAME_MIN_LENGTH, USER_LAST_NAME_MAX_LENGTH, USER_LAST_NAME_MIN_LENGTH,
               USER_NAME_MAX_LENGTH, USER_NAME_MIN_LENGTH, USER_PASSWORD_MIN_LENGTH, REGEX_EMAIL, REGEX_PASSWORD, REGEX_USERNAME, REGEX_UUID4)


@post("/signup")
def _():
    conn = mysql.connector.connect(**g.DB_CONFIG)
    db = conn.cursor(dictionary=True)
    response.set_header(
        "Cache-Control", "no-cache, no-store, must-revalidate")
    # VALIDATION
    user_email = request.forms.get("user_email")
    ##############################
    # username
    if not request.forms.get("user_name"):
        response.status = 400
        return redirect(f"/?error=user_name&user_email={user_email}")

    user_name = request.forms.get("user_name")

    if len(user_name) < USER_NAME_MIN_LENGTH or len(user_name) > USER_NAME_MAX_LENGTH:
        response.status = 400
        return redirect(f"/?error=user_name&user_email={user_email}")
    if not re.match(REGEX_USERNAME, user_name):
        response.status = 400
        return redirect(f"/?error=user_name&user_email={user_email}")

    query_username = f"""
            SELECT *
            FROM users
            WHERE user_name = %(user_name)s
        """
    db.execute(query_username, {"user_name": user_name})
    is_username_taken = db.fetchone()

    if is_username_taken:
        response.status = 400
        return redirect(f"/?error=user_name&user_email={user_email}")

    ##############################
    # Full name validate

    if not request.forms.get("user_first_name"):
        response.status = 400
        return redirect(f"/?error=user_first_name&user_email={user_email}")

    user_first_name = request.forms.get("user_first_name")

    if len(user_first_name) < USER_FIRST_NAME_MIN_LENGTH:
        response.status = 400
        return redirect(f"/?error=user_first_name&user_email={user_email}")
    if len(user_first_name) > USER_FIRST_NAME_MAX_LENGTH:
        response.status = 400
        return redirect(f"/?error=user_first_name&user_email={user_email}")

    if not request.forms.get("user_last_name"):
        response.status = 400
        return redirect(f"/?error=user_last_name&user_email={user_email}")

    user_last_name = request.forms.get("user_last_name")

    if len(user_last_name) < USER_LAST_NAME_MIN_LENGTH:
        response.status = 400
        return redirect(f"/?error=user_last_name&user_email={user_email}")
    if len(user_last_name) > USER_LAST_NAME_MAX_LENGTH:
        response.status = 400
        return redirect(f"/?error=user_last_name&user_email={user_email}")

    ##############################
    # Email validation
    if not request.forms.get("user_email"):
        response.status = 400
        return redirect(f"/?error=user_email")

    if not re.match(REGEX_EMAIL, user_email):
        response.statis = 400
        return redirect(f"/?error=user_email")

    query_email = f"""
        SELECT *
        FROM users
        WHERE user_email = %(user_email)s
    """

    db.execute(query_email, {"user_email": user_email})
    is_email_registered = db.fetchone()

    if is_email_registered:
        response.status = 400
        return {"info": "Email already exists"}

    ##############################
    # Password validation

    if not request.forms.get("user_password"):
        response.status = 400
        return redirect(f"/?error=user_password&user_email={user_email}")

    user_password = request.forms.get("user_password")

    if len(user_password) < USER_PASSWORD_MIN_LENGTH:
        response.status = 400
        return redirect(f"/?error=user_password&user_email={user_email}")

    if not re.match(REGEX_PASSWORD, user_password):
        response.status = 400
        return redirect(f"/?error=user_password&user_email={user_email}")

    # Default picture for everybory
    user_img = "../images/default.jpeg"
    # Create User
    user = {
        "user_id": str(uuid.uuid4()),
        "user_name": user_name,
        "user_first_name": user_first_name,
        "user_last_name": user_last_name,
        "user_email": user_email,
        "user_password": user_password,
        "user_img": user_img
    }

    db.execute("""
        
            INSERT INTO users (user_id, user_name, user_first_name, user_last_name, user_email, user_password, user_img)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(user.values()))

    conn.commit()
    conn.close()

    token = jwt.encode(
        payload=user, key="super_secret", algorithm="HS256")

    response.set_cookie("token", token)

    print("user created")
    return redirect("/home")
    # return redirect(f"/home?user_email={user_email}&user_name={user_name}&user_last_name={user_last_name}")
    # return f"/index?user-email={user_email}&user-name={user_name}&user-last-name={user_last_name}"
