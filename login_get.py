import imp
from bottle import get, request, view
import g
import mariadb


@get("/login")
@view("login")
def _():
    try:
        error = request.params.get("error")
        user_email = request.params.get("user_email")
        user_password = request.params.get("user_password")

        is_xhr = True if request.headers.get('spa') else False

        return dict(title="Login", url="/login", is_xhr=is_xhr, error=error, user_email=user_email, user_password=user_password)
    except Exception as ex:
        print(ex)
    finally:
        print("something")
