from bottle import post, redirect, request
import g

import mariadb

@post("/signup")

def _():

    # VALIDATION
    


    user_name = request.forms.get("user_name")
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    user_img = "../images/default.jpeg"
    #key-value pair
    user = {
        "user_name":user_name,
        "user_first_name":user_first_name,
        "user_last_name":user_last_name,
        "user_email":user_email,
        "user_password":user_password,
        "user_img":user_img
    }

    conn = mariadb.connect(**g.DB_CONFIG)
    db = conn.cursor()

    db.execute("""
        
            INSERT INTO users (user_name, user_first_name, user_last_name, user_email, user_password, user_img)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, tuple(user.values()))

    conn.commit()
    conn.close()
    # g.USERS.append(user)
    return redirect("/home")
    # return redirect(f"/home?user_email={user_email}&user_name={user_name}&user_last_name={user_last_name}")
    # return f"/index?user-email={user_email}&user-name={user_name}&user-last-name={user_last_name}"
    
