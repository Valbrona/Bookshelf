# Bookshelf_LocallyStored

## About the Bookshelf App:
* the following repository contains two Python files: the first one representing the program, while the second one represents the API.
  
* the user can choose one of the 5 listed options:
  
* -> 'a' to add a new book
* -> 'l' to list all books
* -> 'r' to mark a book as read
* -> 'd' to delete a book
* -> 'q' to quit
  
* if the user enters another input, then "Unknown command. Please try again." will be printed out, and the user will need to input a valid command
  
* if the option is "a", then the input added will then be sent to the "check_if_number" function, which contains a nested "check_if_exists" function and will check if the user typed in a valid input and/or if the book already exists, and only appends it to the "books" list, if the book has not been added earlier.
  
* if the user types "l", if there is no book saved on the bookshelf yet, the program will print out "There is no book on your bookshelf yet.", but if there are, they will be printed out and the status will also be shown.
  
* if the user chooses "r", the user will be prompted to add input the book's title, and the it will be sent to the "mark_book_as_read" function. The function is devided into two parts: after user's input has been compared with the book's name, if the book is in the list, it will be marked as read (not only it will be printed out here, but the change can also be checked when typing "l" into the console to list all the books). If the user_input does not match the book['name'], then the user will be informed about it and the user will also have the possibility to add it to the list, by typing "y" or "n" and skip the next lines of code.
  
* if "d" was typed in, the user will be asked to provide a book's title, and the input will be sent to "delete_book" function, where it will be checked, if the user's input matches the book's name, and the book will therefore be removed from the list, but if not, the user will be informed, that the mentioned book was not included on the list.

* if the user types in "q", the app will be termianted.
