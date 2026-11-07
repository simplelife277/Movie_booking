from database import create_connection


def register_user():
    print("\n========== USER REGISTRATION ==========")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO users (name, email, phone)
                VALUES (%s, %s, %s)
            """

            values = (name, email, phone)

            cursor.execute(query, values)
            connection.commit()

            print("\nRegistration successful! 🎉")
            print("User ID:", cursor.lastrowid)

        except Exception as error:
            connection.rollback()
            print("\nRegistration failed:", error)

        finally:
            cursor.close()
            connection.close()


def login_user():
    print("\n========== USER LOGIN ==========")

    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            query = """
                SELECT user_id, name
                FROM users
                WHERE email = %s AND phone = %s
            """

            values = (email, phone)

            cursor.execute(query, values)

            user = cursor.fetchone()

            if user:
                print("\nLogin successful! 🎉")
                print("Welcome,", user[1])
                print("User ID:", user[0])

                return user[0]

            else:
                print("\nInvalid email or phone number ❌")
                return None

        except Exception as error:
            print("\nLogin failed:", error)
            return None

        finally:
            cursor.close()
            connection.close()