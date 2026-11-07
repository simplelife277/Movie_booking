from users import register_user, login_user
from movies import view_movies
from shows import view_shows
from booking import book_ticket, view_my_bookings


def user_menu(user_id):
    while True:
        print("\n========== USER MENU ==========")
        print("1. View Movies")
        print("2. View Shows")
        print("3. Book Ticket")
        print("4. My Bookings")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_movies()

        elif choice == "2":
            view_shows()

        elif choice == "3":
            book_ticket(user_id)

        elif choice == "4":
            view_my_bookings(user_id)

        elif choice == "5":
            print("\nLogged out successfully. 👋")
            break

        else:
            print("\nInvalid choice. Please try again.")


def main():
    while True:

        print("\n================================")
        print("     MOVIE BOOKING SYSTEM")
        print("================================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            user_id = login_user()

            if user_id:
                user_menu(user_id)

        elif choice == "3":
            print("\nThank you for using Movie Booking System! 🎬")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()