from bottle import post, redirect, request, response
import g
import re
import uuid
import mariadb
import jwt

@post("/login")

def _():
  #VALIDATION
  if not request.forms.get("user_email"):
    return redirect("/login?error=user_email")
  if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect("/login?error=user_email")

  user_email = request.forms.get("user_email")
  user_password = request.forms.get("user_password")

  conn = mariadb.connect(**g.DB_CONFIG)
  db = conn.cursor(dictionary=True)

  db.execute("""
  SELECT * FROM users WHERE user_email = %s AND user_password = %s
  """,(user_email, user_password))

  account = db.fetchone()

  print("Account "*5)
  print(account)
  
  #VALIDATE PASSWORD
  if not request.forms.get("user_password"):
    return redirect(f"/login?error=user_password&user_email={user_email}")
  
  if account is not None:
    # create a JWT to set as cookie
    token = jwt.encode(
      payload = account,
      key = "super_secret"
    )

    response.set_cookie("token", token)
    # is_xhr = True if request.headers.get('spa') else False
    redirect ("/home")
    return "Logged in"
    # return dict(title="Login", url="/login", is_xhr=is_xhr)
  else:


    #WRONG PASSWORD
    return redirect(f"/login?error=user_password&user_email={user_email}")
