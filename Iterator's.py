#What Are Iterator's
"""
Iterator's break the large amount of data into chunks.
"""
#How the iterator's Can Be Build?
"Iterators can be build based of two protocol's"

#1 __iter__()
#2 __next__()

for i in range(10):
    print(i)

l = ["Rixz", "Rox", "Rex", "Candy"]
for i in l:
    print(i)


lx = ["Rixz", "Rox", "Rex", "Candy"]

it = iter(lx)

print(next(it))  # Rixz
print(next(it))  # Rox
print(next(it))  # Rex
print(next(it))  # Candy
#What Are Generator's
"""Return the values one at a time and saves the memory """
"""When We Create A Generator We USe "Yield" instead of return"""
def f1():
    yield 1
    yield 2
    yield 3
    yield 4
print(f1)
gen = f1()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#help()- Give Details About particular Topic/Object-
#Dir()- Give Attibute And Function Which We Can Apply.
#Check the String is alphanumerical
print("Rixz123".isalnum())   # True
print("Rixz 123".isalnum()) # False (space)
print("123".isalnum())      # True
print("Rixz!".isalnum())    # False (!)



# MASTER THESE THING AND CONTINUE:---

"""

1. numerical data types
2. arithmetic operations
3. types of errors
4. variables and syntax for variables
5. input() and data type conversions
6. strings and indices (+ve, -ve, default)
7. conditional statements (if--elif--else)
8. usage of logical operators
9. loops -- (for, while loop)
10. control structures of the loops
11. collections or iterables -- list, tuple, set, dictionary
12. functions (args and kwargs)
13. list comprehension, lambda function, map, filter


"""