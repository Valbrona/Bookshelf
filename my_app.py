from utils import my_database

user_choice = """
-> 'a' to add a new book
-> 'l' to list all books
-> 'r' to mark a book as read
-> 'd' to delete a book
-> 'q' to quit

Your choice: """

def menu():
    user_input = input(user_choice)
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "r":
            prompt_read_books()
        elif user_input == "d":
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")
        user_input = input(user_choice)


def prompt_add_book():
    user_book = input("Please type the name of the desired book: ").title()
    user_author = input("Please type the name of the author: ").title()

    my_database.check_if_number(user_book, user_author)


def list_books():
    my_database.get_all_books()


def prompt_read_books():
    user_input =  input("Please write the name of the book you want to mark as 'read': ").title()

    my_database.mark_book_as_read(user_input)


def prompt_delete_book():
    user_input = input("Type in the name of the book you want to remove: ").title()

    my_database.delete_book(user_input)

menu()