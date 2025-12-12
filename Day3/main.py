# -------------------------------
# 1) String Format Method (.format)
# -------------------------------

item = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
price_each = int(input("Enter the price: "))

notification = """Your order for {} is confirmed
Quantity = {}
Price = {}/-""".format(item, quantity, price_each * quantity)

print(notification)


# -------------------------------
# 2) Second String Method (format directly on string)
# -------------------------------

item = input("Enter the item name: ")
Quantity = int(input("Enter the quantity: "))
price_each = int(input("Enter the price: "))

notification2 = """Your order for {} is confirmed
Quantity = {}
Price = {}/-""".format(item, Quantity, price_each * Quantity)

print(notification2)


# -------------------------------
# 3) f-string Method  (BEST METHOD)
# -------------------------------

item = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
price_each = int(input("Enter the price: "))

notification3 = f"""Your order for {item} is confirmed
Quantity = {quantity}
Price = {price_each * quantity}/-"""

print(notification3)


# -------------------------------
# Escape Characters
# -------------------------------

a = "Candy \"the Crush\" Crush"
print(a)


# -------------------------------
# Round Method
# -------------------------------

print(round(10.89))              # Rounds to nearest whole number
print(round(56.344343, 3))       # Rounds to 3 decimal places
print(round(12345.893748, -5))   # Rounds to nearest 100000
