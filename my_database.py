books = []

def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})

def check_if_number(user_book, user_author):
    while user_book.isnumeric() or user_author.isnumeric():
        print("^" * 20)
        print("Please provide a book and author name.")
        user_book = input("Please type the name of the desired book: ").title()
        user_author = input("Please type the name of the author: ").title()

    def check_if_exists():
        nonlocal user_book
        nonlocal user_author
        for book in books:
            if user_book == book["name"] and user_author == book["author"]:
                print(f"<<{user_book}>> written by <<{user_author}>> has already been added yo your list")
                break
        else:
            add_book(user_book, user_author)

    check_if_exists()


def get_all_books():
    num = 0
    for book in books:
        if len(books) > 0:
            print("*" * 10, "Your book collection:", "*" * 10)
            read = "read" if book["read"] else "not read"
            num += 1
            print(f"{num}.{book["name"]} written by {book["author"]} -> STATUS: {read}.")
            break
    else:
        print("There is no book on your bookshelf yet.")


def mark_book_as_read(user_input):
    for book in books:
        if book["name"] == user_input:
            book["read"] = True
            print(f"{book["name"]} is now marked as 'read'.")
            print("*" * 20)
            break
    else:
        user_info = input(
            "The mentioned book is not on your list. Would you like to add it? Type 'y' for YES and 'n' for NO: ")
        if user_info != "y":
            print("_" * 20)
        else:
            user_book = input("Please type the name of the desired book: ").title()
            user_author = input("Please type the name of the author: ").title()

            check_if_number(user_book, user_author)


def delete_book(user_input):
    global books
    books = [book for book in books]
    for book in books:
        if book["name"] == user_input:
            removed_book = books.remove(book)
            print(f"The desired book <{user_input}> has been removed from your list.")
            return removed_book
    else:
        print(f"The mentioned book <{user_input}> is not included on your list.")



