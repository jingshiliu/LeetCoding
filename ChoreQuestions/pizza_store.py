pizza_price = {
    "small": 5.99,
    "medium": 11.99,
    "large": 12.99,
}

total_price = 0

# Ask for pizza size
print("What size of pizza do you want?")
size = input("Size: ")
while size not in pizza_price:
    print("Please enter small, medium, or large size.")
    size = input("Size: ")

toppings = []
while True:
    topping = input("Topping: ")
    if topping == "complete order":
        break
    toppings.append(topping)

print(f"\n\nYou ordered a {size} pizza")
print(f"With {len(toppings)} toppings")
print(f"Toppings are: {', '.join(toppings)}")
print(f"Total: ${pizza_price[size] + 0.99 * len(toppings)}")