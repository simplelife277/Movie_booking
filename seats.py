from database import create_connection


def add_seat():
    print("\n========== ADD SEAT ==========")

    screen_id = input("Enter screen ID: ")
    seate_number = input("Enter seat number: ")

    print("\nSeat Types:")
    print("1. REGULAR")
    print("2. PREMIUM")
    print("3. REPREMIUM")

    type_choice = input("Enter seat type: ")

    if type_choice == "1":
        seate_type = "REGULAR"
    elif type_choice == "2":
        seate_type = "PREMIUM"
    elif type_choice == "3":
        seate_type = "REPREMIUM"
    else:
        print("Invalid seat type.")
        return

    price = input("Enter seat price: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO seats
                (screen_id, seate_number, seate_type, price)
                VALUES (%s, %s, %s, %s)
            """

            values = (
                screen_id,
                seate_number,
                seate_type,
                price
            )

            cursor.execute(query, values)
            connection.commit()

            print("\nSeat added successfully! 🎟️")
            print("Seat ID:", cursor.lastrowid)

        except Exception as error:
            print("\nFailed to add seat:", error)

        finally:
            cursor.close()
            connection.close()


def view_seats():
    print("\n========== ALL SEATS ==========")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT
                    seate_id,
                    screen_id,
                    seate_number,
                    seate_type,
                    price,
                    status
                FROM seats
                ORDER BY screen_id, seate_number
            """

            cursor.execute(query)

            seats = cursor.fetchall()

            if seats:

                for seat in seats:
                    print("\n-----------------------------")
                    print("Seat ID     :", seat[0])
                    print("Screen ID   :", seat[1])
                    print("Seat Number :", seat[2])
                    print("Seat Type   :", seat[3])
                    print("Price       :", seat[4])
                    print("Status      :", seat[5])

            else:
                print("No seats found.")

        except Exception as error:
            print("\nFailed to display seats:", error)

        finally:
            cursor.close()
            connection.close()


def available_seats():
    print("\n========== AVAILABLE SEATS ==========")

    screen_id = input("Enter screen ID: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT
                    seate_id,
                    seate_number,
                    seate_type,
                    price,
                    status
                FROM seats
                WHERE screen_id = %s
                  AND status = 'AVAILABLE'
                ORDER BY seate_number
            """

            cursor.execute(query, (screen_id,))

            seats = cursor.fetchall()

            if seats:

                for seat in seats:
                    print("\n-----------------------------")
                    print("Seat ID     :", seat[0])
                    print("Seat Number :", seat[1])
                    print("Seat Type   :", seat[2])
                    print("Price       :", seat[3])
                    print("Status      :", seat[4])

            else:
                print("\nNo available seats found ❌")

        except Exception as error:
            print("\nFailed to display available seats:", error)

        finally:
            cursor.close()
            connection.close()


def update_seat_status():
    print("\n========== UPDATE SEAT STATUS ==========")

    seat_id = input("Enter seat ID: ")

    print("\nStatus Options:")
    print("1. AVAILABLE")
    print("2. MAINTENANCE")

    status_choice = input("Enter status: ")

    if status_choice == "1":
        status = "AVAILABLE"
    elif status_choice == "2":
        status = "MAINTENANCE"
    else:
        print("Invalid status.")
        return

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                UPDATE seats
                SET status = %s
                WHERE seate_id = %s
            """

            values = (status, seat_id)

            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("\nSeat status updated successfully! ✅")
            else:
                print("\nSeat ID not found ❌")

        except Exception as error:
            print("\nFailed to update seat:", error)

        finally:
            cursor.close()
            connection.close()


def delete_seat():
    print("\n========== DELETE SEAT ==========")

    seat_id = input("Enter seat ID: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                DELETE FROM seats
                WHERE seate_id = %s
            """

            cursor.execute(query, (seat_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("\nSeat deleted successfully! ✅")
            else:
                print("\nSeat ID not found ❌")

        except Exception as error:
            print("\nFailed to delete seat:", error)

        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":

    while True:

        print("\n========== SEAT MANAGEMENT ==========")
        print("1. Add Seat")
        print("2. View Seats")
        print("3. View Available Seats")
        print("4. Update Seat Status")
        print("5. Delete Seat")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_seat()

        elif choice == "2":
            view_seats()

        elif choice == "3":
            available_seats()

        elif choice == "4":
            update_seat_status()

        elif choice == "5":
            delete_seat()

        elif choice == "6":
            print("Exiting Seat Management...")
            break

        else:
            print("Invalid choice. Please try again.")

