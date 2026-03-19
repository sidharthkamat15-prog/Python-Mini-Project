                                         # Shopping Cart System

cart = []

while True:
    print("\n Shopping Cart Menu")
    print("1. Add Item")
    print("2. View Cart")   
    print("3. Remove Item")
    print("4. Checkout\n")    

    choice = input("\nSelect an option (1-4): ")

    if choice == "1":
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        cart.append((item, qty, price))
        print(f"{item} added to cart.")
        
    elif choice == "2":
        if not cart:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for item, qty, price in cart:
                print(f"{item} - Qty: {qty}, Price: ₹{price}, Subtotal: ₹{qty*price}")

    elif choice == "3":
        item = input("Enter the name of the item to remove: ")
        found = False
        for i in cart:
            if i[0].lower() == item.lower():
                cart.remove(i)
                print(f"{item} removed from cart.")
                found = True
                break
        if not found:
            print(f"{item} not found in cart.")

    elif choice == "4":
        if not cart:
            print("Your cart is empty.")
        else:
            total = sum(qty * price for _, qty, price in cart)
            print("\n----- BILL -----")
            for item, qty, price in cart:
                print(f"{item} - Qty: {qty}, Price: ₹{price}, Subtotal: ₹{qty*price}")
            print(f"TOTAL: ₹{total}")
            print("Thank you for shopping!")
            cart.clear()  

    elif choice == "5":
        print("Exiting Shopping Cart. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


    
    