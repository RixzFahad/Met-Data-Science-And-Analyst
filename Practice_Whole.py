# 1️⃣ Numerical Data Types
"""Find The Data Type Of this Particular Variabl's"""
a = 10
b = 10.5
c = 10+4j
print(type(a))
print(type(b))
print(type(c))

"""Out For This"""
print(type(5/2))

# 2️⃣ Arithmetic Operations
"""Prodict the Output"""
print(10+2*5)
print((10 + 2) * 5)

""" What WIll This Print"""
print(17 // 3, 17 % 3)

# 4️⃣ Variables and Syntax
"""What Will be Output For this"""
xr = rx = 5
print(xr, rx)

# 5️⃣ input() and Data Type Conversion
"""Fix The Code"""
num = int(input("Enter Your Number"))
print(num+5)

"""What Is The Type"""
age = input("Enter age: ")
print(type(age))

# 6️⃣ Strings and Indexing
"""What Is The OutPut For This"""
s = "Python"
print(s[0], s[-1])
"""Also For This"""
print(s[1:4])

# 7️⃣ Conditional Statements
"""What Will Be Printed"""
x = 15
if x > 10:
    print("A")
elif x > 20:
    print("B")
else:
    print("C")

"""Write a condition to check if a number is positive, negative, or zero."""
x = 0
if x > 0:
    print("Number is Positive")
elif x < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# 8️⃣ Logical Operators
"""What Is OutPut For This"""
print(True and False or True)
print(True and True or True)
print(True and False or False)

"""What This Will Return"""
print(not (10 > 5 and 3 < 1))

# 9️⃣ Loops (for & while)
"""What Is OutPut"""
for i in range(3):
    print(i)

"""How many times will this loop run?"""
i = 1
while i <= 5:
    i += 2
    print(i)

# 🔟 Control Structures (break, continue, pass)
"""What Is Output For This"""
for i in range(5):
    if i == 3:
        break
    print(i)

# 1️⃣1️⃣ Collections / Iterables
"""Mutable Data Type"""

"""What Is Output For This"""
d = {"a": "Rixz", "b": "Candy"}
print(d["a"])

# 1️⃣2️⃣ Functions (args & kwargs)
"""What Is Output For This"""
def add(*args):
    return sum(args)

print(add(1, 2, 3))

"""*args Definition"""
def add(*args):
    return sum(args)

print(add(1, 2, 3))  # 6

"""What Is Output For This"""
def info(**kwargs):
    print(kwargs)

info(name="Rixz", age=21)

# 1️⃣3️⃣ List Comprehension, Lambda, Map, Filter
"""Convert this into list comprehension:"""
lst = []
for i in range(5):
    lst.append(i*i)
print(lst)

"""What Is Output For This"""
nums = [1, 2, 3, 4]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
