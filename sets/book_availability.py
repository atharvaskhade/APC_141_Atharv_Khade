# Available books and requested books
available_books = {"Hamlet", "Macbeth", "Odyssey", "Frankenstein", "1984"}
requested_books = {"Macbeth", "Frankenstein", "Dracula", "1984", "The Hobbit"}

# Determine which requested books are available
available_requests = requested_books.intersection(available_books)

# Display results
print("Available books:", available_books)
print("Requested books:", requested_books)
print("Requested books that are available:", available_requests)
