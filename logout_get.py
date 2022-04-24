from bottle import get, redirect, request, response, view


@get("/logout")
def _():
    # remove session id and jwt
    response.delete_cookie('user_session_id')
    response.delete_cookie('token')
    return redirect("/login")
