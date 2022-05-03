from bottle import post, redirect, request, response
import g
import re
import uuid

import mysql.connector
import jwt
from g import REGEX_PASSWORD, REGEX_EMAIL


@post("/login")
def _():

    # VALIDATION
    # Email
    if not request.forms.get("user_email"):
        response.status = 400
        return redirect(f"/?error=user_email")

    user_email = request.forms.get("user_email")

    if not re.match(REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        # return {"info": "Email is not valid"}
        return redirect(f"/?error=user_email")

    # Password
    if not request.forms.get("user_password"):
        response.status = 400
        return {"info": "Missing password"}

    user_password = request.forms.get("user_password")

    # if not re.match(REGEX_PASSWORD, user_password):
    #     response.status = 400
    #     return {"info": "Invalid password"}

    conn = mysql.connector.connect(**g.DB_CONFIG)
    db = conn.cursor(dictionary=True)

    db.execute("""
    SELECT * FROM users WHERE user_email = %s AND user_password = %s
    """, (user_email, user_password))

    account = db.fetchone()

    print("Account "*5)
    print(account)
    print(account["user_name"])
    if account:
        # create a JWT to set as cookie
        token = jwt.encode(
            payload=account, key="super_secret", algorithm="HS256")

        response.set_cookie("token", token)

        if account["user_name"] == "admin":
            print("YOU ARE IN ADMIN MODE")
            redirect("/admin")
        else:
            # is_xhr = True if request.headers.get('spa') else False
            redirect("/home")
            return "Logged in"
            # return dict(title="Login", url="/login", is_xhr=is_xhr)
    else:

        # WRONG PASSWORD
        return redirect(f"/login?error=user_password&user_email={user_email}")
