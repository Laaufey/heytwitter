# from bottle import default_app, get, post, run, static_file, view, request
# import g
# from g import tabs, people, trends, tweets, whoToFollow
# from password import gmail_password

# import mariadb
# import smtplib
# import ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# ##############################
# import admin_get       # GET
# import signup_get      # GET
# import signup_ok_get   # GET
# import login_get       # GET
# import home_get        # GET
# import logout_get      # GET
# import profile_get     # GET

# import signup_post     # POST
# import login_post      # POST
# import tweet_post      # POST
# import tweet_delete    # POST

# ##############################


# @get("/validator.js")
# def _():
#     return static_file("validator.js", root=".")

# ##############################


# @get("/spa.js")
# def _():
#     return static_file("spa.js", root=".")

# ##############################


# @get("/")
# @view("index")
# def _():
#     is_xhr = True if request.headers.get('spa') else False
#     return dict(title="Index", tabs=tabs, tweets=tweets, trends=trends, whoToFollow=whoToFollow, users=g.USERS, is_xhr=is_xhr)

# ##############################


# @get("/app.css")
# def _():
#     return static_file("app.css", root=".")
# ##############################


# @get("/images/<image_name>")
# def _(image_name):
#     return static_file(image_name, root="./images")
# ##############################


# @get("/app.js")
# def _():
#     return static_file("app.js", root=".")
# ##############################


# @get("/send-email")
# def _():
#     sender_email = "catmoms34@gmail.com"
#     receiver_email = "catmoms34@gmail.com"
#     password = gmail_password

#     message = MIMEMultipart("alternative")
#     message["Subject"] = "Laufey"
#     message["From"] = sender_email
#     message["To"] = receiver_email

#     # Create the plain-text and HTML version of your message
#     text = """\
#     Hi,
#     Thank you.
#     """

#     html = """\
#     <html>
#     <body>
#         <p>
#         Hi,<br>
#         <b>How are you?</b><br>
#         </p>
#     </body>
#     </html>
#     """

#     # Turn these into plain/html MIMEText objects
#     part1 = MIMEText(text, "plain")
#     part2 = MIMEText(html, "html")

#     # Add HTML/plain-text parts to MIMEMultipart message
#     # The email client will try to render the last part first
#     message.attach(part1)
#     message.attach(part2)

#     # Create secure connection with server and send email
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         try:
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, message.as_string())
#             return "yes, email sent"
#         except Exception as ex:
#             print("ex")
#             return "uppps... could not send the email"


# ##############################
# try:
#     import production
#     application = default_app()
# except Exception as ex:
#     run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
