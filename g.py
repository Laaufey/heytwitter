ITEMS = [
    {
        "id": "bf9f2cb7-57e0-4305-87fe-626bfb1e766e",
        "name": "a",
        "price": 10
    },
    {
        "id": "e0670650-e3f8-461c-9412-b59f2813d2a2",
        "name": "b",
        "price": 20
    },
    {
        "id": "7c17f450-a79d-420c-86e5-86ab0c25188b",
        "name": "c",
        "price": 30
    }
]

USERS = [
    {
        "user_id": "1",
        "user_email": "l@l.is",
        "user_name": "Laufey",
        "user_first_name": "Laufey",
        "user_last_name": "Hjaltested",
        "user_password": "password"
    }
]

SESSIONS = {}

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

tabs = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id": "home", "href": "home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore",
        "id": "explore", "href": "home"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications",
        "id": "notifications", "href": "home"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages",
        "id": "messages", "href": "home"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks",
        "id": "bookmarks", "href": "home"},
    {"icon": "fas fa-clipboard-list fa-fw",
        "title": "Lists", "id": "lists", "href": "home"},
]

people = [

]

trends = [
    {"category": "Music", "title": "We Won", "tweets_counter": "135K Tweets"},
    {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k tweets"},
    {"category": "Trending in US", "title": "Denim Day",
        "tweets_counter": "40k tweets"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k tweets"},
    {"category": "Russia", "title": "Russia", "tweets_counter": "10k tweets"},
]

whoToFollow = [
    {"name": "Júlíana", "account": "@julianabjort", "img": "julla"},
    {"name": "Laufey", "account": "@laaufey", "img": "laufey"},
]

tweets = []

DB_CONFIG = {
    "host": "127.0.0.1", "port": 8889, "user": "root", "password": "root", "database": "heytwitter"
}

TWEET_TEXT_MIN_LENGTH = 2
TWEET_TEXT_MAX_LENGTH = 255

USER_NAME_MAX_LENGTH = 30
USER_NAME_MIN_LENGTH = 2
USER_FIRST_NAME_MAX_LENGTH = 20
USER_FIRST_NAME_MIN_LENGTH = 2
USER_LAST_NAME_MAX_LENGTH = 20
USER_LAST_NAME_MIN_LENGTH = 2
USER_PASSWORD_MIN_LENGTH = 6
USER_PASSWORD_MAX_LENGTH = 50


REGEX_PASSWORD = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
REGEX_USERNAME = "^[a-zA-Z0-9_-]{4,20}$"
REGEX_UUID4 = "^[0-9a-f]{8}\b-[0-9a-f]{4}\b-[0-9a-f]{4}\b-[0-9a-f]{4}\b-[0-9a-f]{12}$"
