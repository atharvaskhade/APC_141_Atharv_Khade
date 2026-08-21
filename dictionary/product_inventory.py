# Create a dictionary containing product names and quantities
inventory = {
    "Laptop": 15,
    "Mouse": 8,
    "Keyboard": 12,
    "USB Cable": 5,
    "Monitor": 10
}

while True:
    print("\n--- Product Inventory ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Display Low Stock (quantity < 10)")
    print("6. Display All Products")
    print("7. Exit")
    
    choice = input("Enter choice (1-7): ")
    
    if choice == '1':
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        inventory[name] = qty
        print("Product added.")
    elif choice == '2':
        name = input("Enter product name: ")
        if name in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[name] = qty
            print("Quantity updated.")
        else:
            print("Product not found.")
    elif choice == '3':
        name = input("Enter product name to delete: ")
        if name in inventory:
            inventory.pop(name)
            print("Product deleted.")
        else:
            print("Product not found.")
    elif choice == '4':
        name = input("Enter product name to search: ")
        if name in inventory:
            print(f"Product: {name}, Quantity: {inventory[name]}")
        else:
            print("Product not found.")
    elif choice == '5':
        print("\nLow Stock Products (quantity < 10):")
        found = False
        for k, v in inventory.items():
            if v < 10:
                print(f"{k}: {v}")
                found = True
        if not found:
            print("All products have sufficient stock.")
    elif choice == '6':
        print("\nAll Inventory:")
        for k, v in inventory.items():
            print(f"{k}: {v}")
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
