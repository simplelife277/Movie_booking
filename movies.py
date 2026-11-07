from database import create_connection


def add_movie():
    print("\n========== ADD MOVIE ==========")

    movie_name = input("Enter movie name: ")
    language = input("Enter language: ")
    genre = input("Enter genre: ")
    duration = input("Enter duration in minutes: ")
    release_date = input("Enter release date (YYYY-MM-DD): ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO movies
                (movie_name, language, genre, duration, release_date)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                movie_name,
                language,
                genre,
                duration,
                release_date
            )

            cursor.execute(query, values)
            connection.commit()

            print("\nMovie added successfully! 🎬")
            print("Movie ID:", cursor.lastrowid)

        except Exception as error:
            print("\nFailed to add movie:", error)

        finally:
            cursor.close()
            connection.close()


def view_movies():
    print("\n========== AVAILABLE MOVIES ==========")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT movie_id, movie_name, language,
                       genre, duration, release_date
                FROM movies
                ORDER BY movie_id
            """

            cursor.execute(query)

            movies = cursor.fetchall()

            if movies:
                for movie in movies:
                    print("\n-----------------------------")
                    print("Movie ID    :", movie[0])
                    print("Movie Name  :", movie[1])
                    print("Language    :", movie[2])
                    print("Genre       :", movie[3])
                    print("Duration    :", movie[4], "minutes")
                    print("Release Date:", movie[5])
            else:
                print("No movies found.")

        except Exception as error:
            print("\nFailed to display movies:", error)

        finally:
            cursor.close()
            connection.close()


def search_movie():
    print("\n========== SEARCH MOVIE ==========")

    movie_name = input("Enter movie name to search: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT movie_id, movie_name, language,
                       genre, duration, release_date
                FROM movies
                WHERE movie_name LIKE %s
            """

            values = ("%" + movie_name + "%",)

            cursor.execute(query, values)

            movies = cursor.fetchall()

            if movies:
                for movie in movies:
                    print("\n-----------------------------")
                    print("Movie ID    :", movie[0])
                    print("Movie Name  :", movie[1])
                    print("Language    :", movie[2])
                    print("Genre       :", movie[3])
                    print("Duration    :", movie[4], "minutes")
                    print("Release Date:", movie[5])
            else:
                print("\nNo matching movie found ❌")

        except Exception as error:
            print("\nSearch failed:", error)

        finally:
            cursor.close()
            connection.close()


def update_movie():
    print("\n========== UPDATE MOVIE ==========")

    movie_id = input("Enter movie ID to update: ")

    movie_name = input("Enter new movie name: ")
    language = input("Enter new language: ")
    genre = input("Enter new genre: ")
    duration = input("Enter new duration: ")
    release_date = input("Enter new release date (YYYY-MM-DD): ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                UPDATE movies
                SET movie_name = %s,
                    language = %s,
                    genre = %s,
                    duration = %s,
                    release_date = %s
                WHERE movie_id = %s
            """

            values = (
                movie_name,
                language,
                genre,
                duration,
                release_date,
                movie_id
            )

            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("\nMovie updated successfully! ✅")
            else:
                print("\nMovie ID not found ❌")

        except Exception as error:
            print("\nUpdate failed:", error)

        finally:
            cursor.close()
            connection.close()


def delete_movie():
    print("\n========== DELETE MOVIE ==========")

    movie_id = input("Enter movie ID to delete: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                DELETE FROM movies
                WHERE movie_id = %s
            """

            cursor.execute(query, (movie_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("\nMovie deleted successfully! ✅")
            else:
                print("\nMovie ID not found ❌")

        except Exception as error:
            print("\nDelete failed:", error)

        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":

    while True:
        print("\n========== MOVIE MANAGEMENT ==========")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Search Movie")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            update_movie()

        elif choice == "5":
            delete_movie()

        elif choice == "6":
            print("Exiting Movie Management...")
            break

        else:
            print("Invalid choice. Please try again.")

