import moviedatabase
import datetime

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
moviedatabase.create_tables()

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    moviedatabase.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("---- \n")


def print_watched_movie_list(username, movies):
    print(f"--{username}'s watched movies--")
    for movie in movies:
        print(f"{movie[1]}")
    print("--- \n")
        

def prompt_watch_movie():
    username = input("Username:  ")
    movie_id = input("Movie ID:   ")
    moviedatabase.watch_movie(username, movie_id)


def prompt_show_watched_movies():
    username = input("Username:  ")
    movies = moviedatabase.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("That user has no watched movies", movies)
    return moviedatabase.get_watched_movies(username)

def prompt_search_movies():
    search_term = input("Enter the partial movie title:  ")
    movies = moviedatabase.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("Found no movies for that search term!")


def prompt_add_user():
    username = input("Username:  ")
    moviedatabase.add_user(username)


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = moviedatabase.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = moviedatabase.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")



