import datetime
import movie.database as db

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
        title TEXT,
        release_timestamp REAL,
        watched INTEGER
    );"""


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_release_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_release_date.timestamp()
    db.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{movie[0]} (on {human_date})")
    print("---- \n")


def prompt_watch_movie():
    movie_title = input("Enter movie title you've watched: ")
    db.watch_movie(movie_title)


def main():
    database = r"/Users/manishgarg/software/sqlite/database.db"
    # create a database connection
    connection = db.create_connection(database)
    db.create_tables(CREATE_MOVIES_TABLE)
    print(welcome)
    print("-----------------------------------------")
    print(menu)
    while (user_input := input(menu)) != "6":
        if user_input == "1":
            prompt_add_movie()
        elif user_input == "2":
            movies = db.get_movies(True)
            print_movie_list("Upcoming", movies)
        elif user_input == "3":
            movies = db.get_movies()
            print_movie_list("All", movies)
        elif user_input == "4":
            prompt_watch_movie()
        elif user_input == "5":
            movies = db.get_watched_movies()
            print_movie_list("Watched", movies)
        else:
            print("Invalid input, please try again!")

    db.close_connection()


if __name__ == '__main__':
    main()
