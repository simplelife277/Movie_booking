from database import create_connection


def add_show():
    print("\n========== ADD SHOW ==========")

    movie_id = input("Enter movie ID: ")
    screen_id = input("Enter screen ID: ")
    show_date = input("Enter show date (YYYY-MM-DD): ")
    show_time = input("Enter show time (HH:MM:SS): ")
    ticket_price = input("Enter ticket price: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO shows
                (movie_id, screen_id, show_date, show_time, ticket_price)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                movie_id,
                screen_id,
                show_date,
                show_time,
                ticket_price
            )

            cursor.execute(query, values)
            connection.commit()

            print("\nShow added successfully! 🎬")
            print("Show ID:", cursor.lastrowid)

        except Exception as error:
            print("\nFailed to add show:", error)

        finally:
            cursor.close()
            connection.close()


def view_shows():
    print("\n========== AVAILABLE SHOWS ==========")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT
                    s.show_id,
                    m.movie_name,
                    th.theatre_name,
                    sc.screen_name,
                    s.show_date,
                    s.show_time,
                    s.ticket_price,
                    s.status
                FROM shows s
                INNER JOIN movies m
                    ON s.movie_id = m.movie_id
                INNER JOIN screens sc
                    ON s.screen_id = sc.screen_id
                INNER JOIN theatres th
                    ON sc.theatre_id = th.theatre_id
                ORDER BY s.show_date, s.show_time
            """

            cursor.execute(query)

            shows = cursor.fetchall()

            if shows:

                for show in shows:
                    print("\n--------------------------------")
                    print("Show ID      :", show[0])
                    print("Movie        :", show[1])
                    print("Theatre      :", show[2])
                    print("Screen       :", show[3])
                    print("Show Date    :", show[4])
                    print("Show Time    :", show[5])
                    print("Ticket Price :", show[6])
                    print("Status       :", show[7])

            else:
                print("No shows found.")

        except Exception as error:
            print("\nFailed to display shows:", error)

        finally:
            cursor.close()
            connection.close()


def search_shows():
    print("\n========== SEARCH SHOW ==========")

    movie_name = input("Enter movie name: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT
                    s.show_id,
                    m.movie_name,
                    t.theater_name,
                    sc.screen_name,
                    s.show_date,
                    s.show_time,
                    s.ticket_price,
                    s.status
                FROM shows s
                INNER JOIN movies m
                    ON s.movie_id = m.movie_id
                INNER JOIN screens sc
                    ON s.screen_id = sc.screen_id
                INNER JOIN theatres t
                    ON sc.theatre_id = t.theater_id
                ORDER BY s.show_date, s.show_time
            """

            values = ("%" + movie_name + "%",)

            cursor.execute(query, values)

            shows = cursor.fetchall()

            if shows:

                for show in shows:
                    print("\n--------------------------------")
                    print("Show ID      :", show[0])
                    print("Movie        :", show[1])
                    print("Theatre      :", show[2])
                    print("Screen       :", show[3])
                    print("Show Date    :", show[4])
                    print("Show Time    :", show[5])
                    print("Ticket Price :", show[6])
                    print("Status       :", show[7])

            else:
                print("\nNo shows found for this movie ❌")

        except Exception as error:
            print("\nSearch failed:", error)

        finally:
            cursor.close()
            connection.close()


def update_show():
    print("\n========== UPDATE SHOW ==========")

    show_id = input("Enter show ID to update: ")

    show_date = input("Enter new show date (YYYY-MM-DD): ")
    show_time = input("Enter new show time (HH:MM:SS): ")
    ticket_price = input("Enter new ticket price: ")
    status = input(
        "Enter status (AVAILABLE/CANCELLED/COMPLETED): "
    ).upper()

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                UPDATE shows
                SET show_date = %s,
                    show_time = %s,
                    ticket_price = %s,
                    status = %s
                WHERE show_id = %s
            """

            values = (
                show_date,
                show_time,
                ticket_price,
                status,
                show_id
            )

            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("\nShow updated successfully! ✅")
            else:
                print("\nShow ID not found ❌")

        except Exception as error:
            print("\nUpdate failed:", error)

        finally:
            cursor.close()
            connection.close()


def delete_show():
    print("\n========== DELETE SHOW ==========")

    show_id = input("Enter show ID to delete: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                DELETE FROM shows
                WHERE show_id = %s
            """

            cursor.execute(query, (show_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("\nShow deleted successfully! ✅")
            else:
                print("\nShow ID not found ❌")

        except Exception as error:
            print("\nDelete failed:", error)

        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":

    while True:

        print("\n========== SHOW MANAGEMENT ==========")
        print("1. Add Show")
        print("2. View Shows")
        print("3. Search Show")
        print("4. Update Show")
        print("5. Delete Show")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_show()

        elif choice == "2":
            view_shows()

        elif choice == "3":
            search_shows()

        elif choice == "4":
            update_show()

        elif choice == "5":
            delete_show()

        elif choice == "6":
            print("Exiting Show Management...")
            break

        else:
            print("Invalid choice. Please try again.")


