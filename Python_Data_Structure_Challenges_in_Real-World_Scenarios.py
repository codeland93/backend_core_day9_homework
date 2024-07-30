def add_book_to_library(library, new_book):
    if new_book not in library:
        library.append(new_book)
        print(f'Book "{new_book[0]}" by {new_book[1]} added to the library.')
    else:
        print(f'Book "{new_book[0]}" by {new_book[1]} is already in the library and will not be added again.')

# Existing Library Data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Example usage
new_book_1 = ("Fahrenheit 451", "Ray Bradbury")
new_book_2 = ("1984", "George Orwell")

add_book_to_library(library, new_book_1)  # Should add the new book
add_book_to_library(library, new_book_2)  # Should detect the duplicate and not add it

# Print the updated library to verify
print(library)

