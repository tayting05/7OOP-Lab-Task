menu = {
    "Water": 15,
    "Burger": 50,
    "Spaghetti": 75,
    "Soda": 25,
    "Chicken": 60,
    "Steak": 85,
    "Nuggets": 50,
    "Fries": 40,
    "Juice": 25,
    "Pie": 45
}

cart = []
prices = []

print("-------- MENU --------")
for item, price in menu.items():
    print(f"{item:15}: ₱{price}")

while True:
    order = input("Enter a food to buy (q to quit): ").strip().title()
    if order.lower() == "q":
        break
    elif order in menu:
        cart.append(order)
        prices.append(menu[order])
        print(f"Added {order} - ₱{menu[order]}")
    else:
        print("Not Available")

print("\n----- YOUR ORDERS -----")
total = 0
for item, price in zip(cart, prices):
    print(f"{item:15} ₱{price}")
    total += price

print(f"\nYour total is: ₱{total}")
