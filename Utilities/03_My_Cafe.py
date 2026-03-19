                                        # My Cafe

# Café Bliss Ordering System

menu = {
    "Coffee": {
        "Espresso": 120,
        "Americano": 150,
        "Cappuccino": 180,
        "Latte": 200,
        "Mocha": 220
    },
    "Tea": {
        "Masala Tea": 100,
        "Green Tea": 120,
        "Black Tea": 110,
        "Herbal Tea": 130
    },
    "Cold Drinks": {
        "Iced Coffee": 180,
        "Cold Brew": 200,
        "Iced Tea": 150,
        "Lemonade": 120,
        "Smoothie": 250
    },
    "Snacks": {
        "Croissant": 80,
        "Muffin": 90,
        "Sandwich": 150,
        "Pasta": 220,
        "Pizza Slice": 180
    },
    "Desserts": {
        "Brownie": 120,
        "Cheesecake": 200,
        "Ice Cream": 150,
        "Donut": 100
    }
}

def print_menu(menu):
    print("="*40)
    print("        ☕ Welcome to Café Bliss ☕")
    print("="*40)
    item_number = 1
    item_map = {}
    for category, items in menu.items():
        print(f"\n--- {category} ---")
        for item, price in items.items():
            print(f"{item_number}. {item:<20} ₹{price:>5}")
            item_map[item_number] = (item, price)
            item_number += 1
    print("="*40)
    return item_map

def take_order(item_map):
    order = []
    while True:
        choice = input("Enter item number to order (or 'done' to finish): ")
        if choice.lower() == "done":
            break
        if choice.isdigit() and int(choice) in item_map:
            qty = input(f"Enter quantity for {item_map[int(choice)][0]}: ")
            if qty.isdigit():
                order.append((item_map[int(choice)][0], item_map[int(choice)][1], int(qty)))
                print(f"Added {qty} x {item_map[int(choice)][0]} to your order.")
            else:
                print("Invalid quantity. Try again.")
        else:
            print("Invalid choice. Try again.")
    return order

def print_bill(order):
    print("\n" + "="*40)
    print("              🧾 Your Bill 🧾")
    print("="*40)
    total = 0
    for item, price, qty in order:
        line_total = price * qty
        total += line_total
        print(f"{item:<20} x{qty:<3} ₹{line_total:>5}")
    print("="*40)
    print(f"Total Amount: ₹{total}")
    print("="*40)
    print("Thank you for visiting Café Bliss! ☕")

# Main Program
item_map = print_menu(menu)
order = take_order(item_map)
print_bill(order)