# Nothing here yet!

# title, release_date, watched

import sqlite3
import datetime


CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched(
    user_username TEXT,
    movie_id TEXT,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies
JOIN watched ON movies.id = watched.movie_id
JOIN users ON users.username = watched.user_username
WHERE users.username = ?;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""


connection = sqlite3.connect("mymoviedata.db")

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_USERS_TABLE)

def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username, ))

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%", ))
        return cursor.fetchall()

def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))
    

def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username, ))
        return cursor.fetchall()














# INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES(?, ?);"
# INSERT_USER = "INSERT INTO users (username) VALUES (?);"
# DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
# SELECT_ALL_MOVIES = "SELECT * FROM movies;"
# SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
# # SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE user_username = ?;"


# SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies
# JOIN watched ON movies.id = watched.movie_id
# JOIN users ON users.username = watched.user_username
# WHERE users.username = ?;"""
# INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?,?);"
# SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"
# SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE ?;"