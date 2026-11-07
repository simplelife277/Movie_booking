import mysql.connector


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="movie_booking"
        )

        if connection.is_connected():
            print("MySQL Database Connected Successfully!")

        return connection

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        return None


if __name__ == "__main__":
    connection = create_connection()

    if connection:
        connection.close()
        print("Connection Closed.")






