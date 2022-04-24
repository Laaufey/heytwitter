from bottle import post, redirect, request, response
import g
import jwt
import mariadb
import re
from g import (USER_FIRST_NAME_MAX_LENGTH, USER_FIRST_NAME_MIN_LENGTH, USER_LAST_NAME_MAX_LENGTH, USER_LAST_NAME_MIN_LENGTH,
               USER_NAME_MAX_LENGTH, USER_NAME_MIN_LENGTH, USER_PASSWORD_MIN_LENGTH, REGEX_EMAIL, REGEX_PASSWORD, REGEX_USERNAME, REGEX_UUID4)


@post("/signup")
def _():
    conn = mariadb.connect(**g.DB_CONFIG)
    db = conn.cursor(dictionary=True)
    response.set_header(
        "Cache-Control", "no-cache, no-store, must-revalidate")
    # VALIDATION
    ##############################
    # username
    if not request.forms.get("user_name"):
        response.status = 400
        return {"info": "Username is missing"}

    user_name = request.forms.get("user_name")

    if len(user_name) < USER_NAME_MIN_LENGTH:
        response.status = 400
        return {"info": f"Username must be at least {USER_NAME_MIN_LENGTH} characters long"}

    if len(user_name) > USER_NAME_MAX_LENGTH:
        response.status = 400
        return {"info": f"Username can only have a maximum of {USER_NAME_MAX_LENGTH} characters"}

    if not re.match(REGEX_USERNAME, user_name):
        response.status = 400
        return {
            "info": "Username can only have letters from a-z (Uppercase and lowercase), numbers 0-9, underscores and hyphens"
        }

    query_username = f"""
            SELECT *
            FROM users
            WHERE user_name = %(user_name)s
        """
    db.execute(query_username, {"user_name": user_name})
    is_username_taken = db.fetchone()

    if is_username_taken:
        response.status = 400
        return {"info": "Username is taken, try another one"}

    ##############################
    # Full name validate

    if not request.forms.get("user_first_name"):
        response.status = 400
        return {"info": "First name is missing"}

    user_first_name = request.forms.get("user_first_name")

    if len(user_first_name) < USER_FIRST_NAME_MIN_LENGTH:
        response.status = 400
        return {"info": f"Name must be at least {USER_FIRST_NAME_MIN_LENGTH} characters long"}
    if len(user_first_name) > USER_FIRST_NAME_MAX_LENGTH:
        response.status = 400
        return {"info": f"Name can only have a maximum of {USER_FIRST_NAME_MAX_LENGTH} characters"}

    if not request.forms.get("user_last_name"):
        response.status = 400
        return {"info": "Last name is missing"}

    user_last_name = request.forms.get("user_last_name")

    if len(user_last_name) < USER_LAST_NAME_MIN_LENGTH:
        response.status = 400
        return {"info": f"Name must be at least {USER_LAST_NAME_MIN_LENGTH} characters long"}
    if len(user_last_name) > USER_LAST_NAME_MAX_LENGTH:
        response.status = 400
        return {"info": f"Name can only have a maximum of {USER_LAST_NAME_MAX_LENGTH} characters"}

    ##############################
    # Email validation
    if not request.forms.get("user_email"):
        response.status = 400
        return {"info": "Email is missing"}

    user_email = request.forms.get("user_email")

    if not re.match(REGEX_EMAIL, user_email):
        response.statis = 400
        return {"info": "Email is not invalid"}

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
        return {"info": "Password is missing"}

    user_password = request.forms.get("user_password")

    if len(user_password) < USER_PASSWORD_MIN_LENGTH:
        response.status = 400
        return {"info": f"Password must be at least {USER_PASSWORD_MIN_LENGTH} characters long"}

    if not re.match(REGEX_PASSWORD, user_password):
        response.status = 400
        return {
            "info": "Password must be at least 8 characters long, have 1 uppercase letter, 1 lowercase letter and 1 number or 1 symbol"
        }
    # Default picture for everybory
    user_img = "../images/default.jpeg"

    # Create User
    user = {
        "user_name": user_name,
        "user_first_name": user_first_name,
        "user_last_name": user_last_name,
        "user_email": user_email,
        "user_password": user_password,
        "user_img": user_img
    }

    db.execute("""
        
            INSERT INTO users (user_name, user_first_name, user_last_name, user_email, user_password, user_img)
            VALUES (%s, %s, %s, %s, %s, %s)
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
