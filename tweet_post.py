from bottle import post, redirect, request
import g
import uuid

@post("/home")

def _():

    src = "src"
    user_first_name = "user_first_name"
    user_last_name = "user_last_name"
    user_name = "user_name"
    date = "date"
    text = request.forms.get("tweet")
    
    tweet = {
        "src":src,
        "user_first_name":user_first_name,
        "user_last_name":user_last_name,
        "user_name":user_name,
        "date":date,
        "text":text
    }
    g.tweets.append(tweet)

    return redirect("/home")