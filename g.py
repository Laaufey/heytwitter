ITEMS = [
    {
        "id":"bf9f2cb7-57e0-4305-87fe-626bfb1e766e",
        "name":"a",
        "price":10
    },
        {
        "id":"e0670650-e3f8-461c-9412-b59f2813d2a2",
        "name":"b",
        "price":20
    },
    {
        "id":"7c17f450-a79d-420c-86e5-86ab0c25188b",
        "name":"c",
        "price":30
    }
]

USERS = [
{
    "user_id":"1",
    "user_email":"l@l.is",
    "user_name":"Laufey",
    "user_first_name":"Laufey",
    "user_last_name":"Hjaltested",
    "user_password":"password"
}
]

SESSIONS = {}

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

tabs = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
    ]

people = [
    {"src": "stephie.png", "name": "Stephie Jensen", "handle": "@sjensen"},
    {"src": "monk.jpg", "name": "Adrian Monk", "handle": "@detective :)"},
    {"src": "kevin.jpg", "name": "Kevin Hart", "handle": "@miniRock"}
    ]

trends = [
    {"category": "Music", "title": "We Won", "tweets_counter": "135K Tweets"},
    {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k tweets"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k tweets"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k tweets"},
    {"category": "Russia", "title": "Russia", "tweets_counter": "10k tweets"},
    ]

whoToFollow = [
    {"name": "Júlíana", "account": "@julianabjort", "img":"julla"},
    {"name": "Laufey", "account": "@laaufey", "img":"laufey"},
    ]   

tweets = [
    {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
    {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
    {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
    {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
    {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    ]

DB_CONFIG = {
    "host": "127.0.0.1", "port": 8889, "user": "root", "password": "root", "database": "heytwitter" 
}