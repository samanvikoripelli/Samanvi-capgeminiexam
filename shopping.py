cart = []
name = input("enter item name")
price = float(input("enter item price"))
cart.append((name,price))
for item in cart:
    print(f"{item[0]}-${item[1]:.2f}")
total = sum(item[1] for item in cart)
print(f"total: ${total:.2f}")    