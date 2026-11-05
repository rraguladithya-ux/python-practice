<<<<<<< HEAD
import datetime

GST_RATE = 0.05

menu = {
    "Coffee": 40,
    "Tea": 20,
    "Burger": 100,
    "Pizza": 150,
    "Sandwich": 80,
    "French Fries": 70,
    "Milkshake": 90
}

def display_menu():
    print("\n========== CAFE MENU ==========")

    for index, (item, price) in enumerate(menu.items(), 1):
        print(f"{index}. {item} - Rs.{price}")

def generate_bill():

    cart = {}
    subtotal = 0

    while True:

        display_menu()

        choice = input("\nEnter item name (or 'done'): ").strip()

        if choice.lower() == "done":
            break

        item = next(
            (name for name in menu if name.lower() == choice.lower()),
            None
        )

        if item is None:
            print("Invalid item!")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                continue

        except ValueError:
            print("Enter a valid quantity!")
            continue

        cart[item] = cart.get(item, 0) + quantity

    print("\n========== CUSTOMER BILL ==========")

    for item, quantity in cart.items():

        price = menu[item]
        total = price * quantity

        subtotal += total

        print(f"{item:15} x {quantity} = Rs.{total}")

    gst = subtotal * GST_RATE
    grand_total = subtotal + gst

    print("-----------------------------------")
    print(f"Subtotal:       Rs.{subtotal:.2f}")
    print(f"GST (5%):       Rs.{gst:.2f}")
    print(f"Grand Total:    Rs.{grand_total:.2f}")
    print("-----------------------------------")
    print("Thank you! Visit Again!")

=======
import datetime

GST_RATE = 0.05

menu = {
    "Coffee": 40,
    "Tea": 20,
    "Burger": 100,
    "Pizza": 150,
    "Sandwich": 80,
    "French Fries": 70,
    "Milkshake": 90
}

def display_menu():
    print("\n========== CAFE MENU ==========")

    for index, (item, price) in enumerate(menu.items(), 1):
        print(f"{index}. {item} - Rs.{price}")

def generate_bill():

    cart = {}
    subtotal = 0

    while True:

        display_menu()

        choice = input("\nEnter item name (or 'done'): ").strip()

        if choice.lower() == "done":
            break

        item = next(
            (name for name in menu if name.lower() == choice.lower()),
            None
        )

        if item is None:
            print("Invalid item!")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                continue

        except ValueError:
            print("Enter a valid quantity!")
            continue

        cart[item] = cart.get(item, 0) + quantity

    print("\n========== CUSTOMER BILL ==========")

    for item, quantity in cart.items():

        price = menu[item]
        total = price * quantity

        subtotal += total

        print(f"{item:15} x {quantity} = Rs.{total}")

    gst = subtotal * GST_RATE
    grand_total = subtotal + gst

    print("-----------------------------------")
    print(f"Subtotal:       Rs.{subtotal:.2f}")
    print(f"GST (5%):       Rs.{gst:.2f}")
    print(f"Grand Total:    Rs.{grand_total:.2f}")
    print("-----------------------------------")
    print("Thank you! Visit Again!")

>>>>>>> 14009ed88a480391cc7ab1c07a5518bf796beabf
generate_bill()