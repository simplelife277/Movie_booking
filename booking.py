from database import create_connection


def book_ticket(user_id):
    print("\n========== BOOK MOVIE TICKET ==========")

    show_id = input("Enter show ID: ")
    total_seats = input("Enter number of tickets: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            # Check show and get ticket price
            query = """
                SELECT show_id, ticket_price
                FROM shows
                WHERE show_id = %s
                  AND status = 'AVAILABLE'
            """

            cursor.execute(query, (show_id,))
            show = cursor.fetchone()

            if not show:
                print("\nShow not found or unavailable ❌")
                return

            ticket_price = float(show[1])
            total_seats = int(total_seats)

            if total_seats <= 0:
                print("\nNumber of tickets must be greater than 0.")
                return

            # Calculate total amount
            total_amount = ticket_price * total_seats

            print("\n========== BOOKING DETAILS ==========")
            print("Show ID       :", show_id)
            print("Ticket Price  :", ticket_price)
            print("Total Tickets :", total_seats)
            print("Total Amount  :", total_amount)

            confirm = input("\nConfirm booking? (yes/no): ").lower()

            if confirm != "yes":
                print("\nBooking cancelled.")
                return

            # Insert booking
            insert_query = """
                INSERT INTO bookings
                (user_id, show_id, total_seats, total_amount)
                VALUES (%s, %s, %s, %s)
            """

            values = (
                user_id,
                show_id,
                total_seats,
                total_amount
            )

            cursor.execute(insert_query, values)
            connection.commit()

            print("\n========== BOOKING SUCCESSFUL ==========")
            print("Booking ID   :", cursor.lastrowid)
            print("Show ID      :", show_id)
            print("Total Tickets:", total_seats)
            print("Total Amount :", total_amount)
            print("Status       : CONFIRMED 🎉")

        except ValueError:
            print("\nPlease enter valid numbers.")

        except Exception as error:
            connection.rollback()
            print("\nBooking failed:", error)

        finally:
            cursor.close()
            connection.close()


def view_my_bookings(user_id):
    print("\n========== MY BOOKINGS ==========")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT
                    b.booking_id,
                    m.movie_name,
                    s.show_date,
                    s.show_time,
                    b.total_seats,
                    b.total_amount,
                    b.booking_date
                FROM bookings b
                INNER JOIN shows s
                    ON b.show_id = s.show_id
                INNER JOIN movies m
                    ON s.movie_id = m.movie_id
                WHERE b.user_id = %s
                ORDER BY b.booking_id DESC
            """

            cursor.execute(query, (user_id,))

            bookings = cursor.fetchall()

            if bookings:

                for booking in bookings:
                    print("\n-----------------------------")
                    print("Booking ID   :", booking[0])
                    print("Movie        :", booking[1])
                    print("Show Date    :", booking[2])
                    print("Show Time    :", booking[3])
                    print("Total Tickets:", booking[4])
                    print("Total Amount :", booking[5])
                    print("Booked On    :", booking[6])

            else:
                print("\nNo bookings found.")

        except Exception as error:
            print("\nFailed to load bookings:", error)

        finally:
            cursor.close()
            connection.close()

