# Create a dictionary containing book IDs and book names
books = {
    "B01": "To Kill a Mockingbird",
    "B02": "1984",
    "B03": "The Great Gatsby"
}

while True:
    print("\n--- Book Manager ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Total Books")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        book_id = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        books[book_id] = book_name
        print("Book added.")
    elif choice == '2':
        book_id = input("Enter book ID to search: ")
        if book_id in books:
            print(f"Book ID: {book_id}, Book Name: {books[book_id]}")
        else:
            print("Book not found.")
    elif choice == '3':
        book_id = input("Enter book ID to remove: ")
        if book_id in books:
            removed_book = books.pop(book_id)
            print(f"Removed Book: '{removed_book}'")
        else:
            print("Book not found.")
    elif choice == '4':
        print("\nAll Books:")
        for book_id, book_name in books.items():
            print(f"{book_id}: {book_name}")
    elif choice == '5':
        print(f"\nTotal number of books: {len(books)}")
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
