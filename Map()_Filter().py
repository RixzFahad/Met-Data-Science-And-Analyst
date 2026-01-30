# ============================================================
# FUNCTIONS ARE FIRST-CLASS OBJECTS IN PYTHON
# ============================================================
# Meaning:
# 1. A function can be assigned to a variable
# 2. A function can be passed as an argument to another function
# 3. A function can be returned from another function
# 4. A function can be stored inside data structures
# ============================================================


# ------------------------------------------------------------
# Example 1: Find even numbers using a normal loop
# ------------------------------------------------------------
l = [24, 45, 22, 56, 77, 66, 88]
even_list = []

for i in l:
    if i % 2 == 0:
        even_list.append(i)

print("Even numbers using loop:", even_list)


# ------------------------------------------------------------
# Example 2: Find even numbers using list comprehension
# ------------------------------------------------------------
even_list_comp = [i for i in l if i % 2 == 0]
print("Even numbers using list comprehension:", even_list_comp)


# ------------------------------------------------------------
# Example 3: Function to check even number
# ------------------------------------------------------------
# This function returns:
# - the number if it is even
# - False if it is odd
def check_even(num):
    if num % 2 == 0:
        return num
    else:
        return False


# ------------------------------------------------------------
# Example 4: map() function (Function as First-Class Object)
# ------------------------------------------------------------
# map() takes a function as an argument and applies it
# to every element in the iterable
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

m1 = list(map(check_even, l))
print("Using map() with function:", m1)

# NOTE:
# Here check_even is passed WITHOUT ()
# This proves functions are first-class objects


# ------------------------------------------------------------
# Example 5: Taking multiple user inputs
# ------------------------------------------------------------
user = input("Enter numbers separated by space: ").split()
print("User input (string list):", user)


# ------------------------------------------------------------
# Example 6: Convert user input to integers (using loop)
# ------------------------------------------------------------
print("Converted to integers using loop:")
for i in user:
    print(int(i))


# ------------------------------------------------------------
# Example 7: Convert user input using map()
# ------------------------------------------------------------
# map() is best when handling multiple inputs
m2 = tuple(map(int, user))
print("Converted using map():", m2)


# ------------------------------------------------------------
# Example 8: Lambda function
# ------------------------------------------------------------
# Lambda is an anonymous function written in one line
# Syntax: lambda arguments : expression

# Using lambda with map()
m3 = list(map(lambda num: num % 2 == 0, l))
print("Using lambda with map():", m3)


# ------------------------------------------------------------
# Example 9: filter() function
# ------------------------------------------------------------
# filter() returns only values where condition is True
f1 = list(filter(lambda num: num % 2 == 0, l))
print("Using filter() to get even numbers:", f1)


# ------------------------------------------------------------
# FINAL NOTES:
# ------------------------------------------------------------
# map()    -> transforms each element
# filter() -> selects elements based on condition
# lambda  -> short anonymous function
# Functions are first-class objects because they can be:
# passed, stored, returned, and assigned like variables
# ------------------------------------------------------------
