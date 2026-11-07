from database import create_connection


def add_theatre():
    print("\n========== ADD THEATRE ==========")

    theatre_name = input("Enter theatre name: ")
    location = input("Enter location: ")
    city = input("Enter city: ")
    total_screen = input("Enter total number of screens: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO theatres
                (theater_name, location, city, total_screen)
                VALUES (%s, %s, %s, %s)
            """

            values = (
                theatre_name,
                location,
                city,
                total_screen
            )

            cursor.execute(query, values)
            connection.commit()

            print("\nTheatre added successfully! 🎬")
            print("Theatre ID:", cursor.lastrowid)

        except Exception as error:
            print("\nFailed to add theatre:", error)

        finally:
            cursor.close()
            connection.close()


def view_theatres():
    print("\n========== THEATRES ==========")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT theater_id, theater_name,
                       location, city, total_screen
                FROM theatres
                ORDER BY theater_id
            """

            cursor.execute(query)

            theatres = cursor.fetchall()

            if theatres:
                for theatre in theatres:
                    print("\n-----------------------------")
                    print("Theatre ID   :", theatre[0])
                    print("Theatre Name :", theatre[1])
                    print("Location     :", theatre[2])
                    print("City         :", theatre[3])
                    print("Total Screens:", theatre[4])
            else:
                print("No theatres found.")

        except Exception as error:
            print("\nFailed to display theatres:", error)

        finally:
            cursor.close()
            connection.close()


def search_theatre():
    print("\n========== SEARCH THEATRE ==========")

    city = input("Enter city to search: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT theater_id, theater_name,
                       location, city, total_screen
                FROM theatres
                WHERE city LIKE %s
            """

            values = ("%" + city + "%",)

            cursor.execute(query, values)

            theatres = cursor.fetchall()

            if theatres:
                for theatre in theatres:
                    print("\n-----------------------------")
                    print("Theatre ID   :", theatre[0])
                    print("Theatre Name :", theatre[1])
                    print("Location     :", theatre[2])
                    print("City         :", theatre[3])
                    print("Total Screens:", theatre[4])
            else:
                print("\nNo theatre found in this city ❌")

        except Exception as error:
            print("\nSearch failed:", error)

        finally:
            cursor.close()
            connection.close()


def update_theatre():
    print("\n========== UPDATE THEATRE ==========")

    theatre_id = input("Enter theatre ID to update: ")

    theatre_name = input("Enter new theatre name: ")
    location = input("Enter new location: ")
    city = input("Enter new city: ")
    total_screen = input("Enter new total screens: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                UPDATE theatres
                SET theater_name = %s,
                    location = %s,
                    city = %s,
                    total_screen = %s
                WHERE theater_id = %s
            """

            values = (
                theatre_name,
                location,
                city,
                total_screen,
                theatre_id
            )

            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("\nTheatre updated successfully! ✅")
            else:
                print("\nTheatre ID not found ❌")

        except Exception as error:
            print("\nUpdate failed:", error)

        finally:
            cursor.close()
            connection.close()


def delete_theatre():
    print("\n========== DELETE THEATRE ==========")

    theatre_id = input("Enter theatre ID to delete: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                DELETE FROM theatres
                WHERE theater_id = %s
            """

            cursor.execute(query, (theatre_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("\nTheatre deleted successfully! ✅")
            else:
                print("\nTheatre ID not found ❌")

        except Exception as error:
            print("\nDelete failed:", error)

        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":

    while True:
        print("\n========== THEATRE MANAGEMENT ==========")
        print("1. Add Theatre")
        print("2. View Theatres")
        print("3. Search Theatre")
        print("4. Update Theatre")
        print("5. Delete Theatre")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_theatre()

        elif choice == "2":
            view_theatres()

        elif choice == "3":
            search_theatre()

        elif choice == "4":
            update_theatre()

        elif choice == "5":
            delete_theatre()

        elif choice == "6":
            print("Exiting Theatre Management...")
            break

        else:
            print("Invalid choice. Please try again.")