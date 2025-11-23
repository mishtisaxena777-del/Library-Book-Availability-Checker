# library book management system using dictionaries and tuples
books = {
    '978-3-45-678901-2': {'title': 'Book A', 'author': 'Author A', 'available': True},
    '978-1-23-456789-7': {'title': 'Book B', 'author': 'Author B', 'available': True},
    '978-0-12-345678-9': {'title': 'Book C', 'author': 'Author C', 'available': False},
}

def check_availability(isbn):
    if isbn in books:
        if books[isbn]['available']:
            return f"{books[isbn]['title']} is available."
        else:
            return f"{books[isbn]['title']} is currently checked out."
    else:
        return "Book not found in the library."

# Example usage:
isbn_input = input("Enter ISBN to check availability: ")
result = check_availability(isbn_input)
print(result)
    