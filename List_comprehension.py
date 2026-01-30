#List Comprehension :- If offer smaller line of code where,
# a new list is created from existing list


My = ["Rixz", "Rexx", "Roxx", "Rixx","Roxz"]
new = []
#print the my where my have letter e there.
for i in My:
    if "i" in i:
        new.append(i)
print(new)

#seprate the even number in a new list by using the LC
li = [1,2,3,4,5,6,7]
new2 = [i for i in li if i%2==0]
print(new2)

#print the square of even number above the list
li2= [i**2 for i in li if i%2==0]
print(li2)

# Print the My iN upperCAse
MyUpper = [i.upper() for i in My if "i" in i]
print(MyUpper)


# Lamba-Function:-  Lambda is a anoymous function it take pass multiple arguements but only takes
#one Expression.


#What are expression?
"""The Step We use to give a output is known as expression"""

def f1():
    return "Hello"
print(f1())

#SYNTAX:- Lambda Arguement : Single Expression

a = lambda x,y: x+y
print(a(10,5))

b = lambda x,y,z : (x+10, y+20, z+30)
print(b(5,10,15))


# Find the square , cube and square root by using lammbda.
def square (num):
    return num**2
def cube(num):
    return num**3
def sqrt(num):
    return num**0.5
print(square(5))
print(cube(2))
print(sqrt(25))


# Second Method to do this by using Lambda Function().
def power(n):
    return lambda x:x**n
square = power(2)
cube = power(3)
sqrt = power(0.5)
print(square(5))
print(cube(2))
print(sqrt(250))
# We Use Lamba Inside a Function to make it faster.

# def power(num):
#     return lambda
# print(power(2))


# Map Function :- Map Function takes a function,
# as an arguement and run over each element in the collection


Watashi = ["Rixz", "Rexx", "Roxx", "Rixx","Roxz"]

Watashi1 = [23,45,67,7,88,76]
# PRint the each item length in the list

new = []
for i in Watashi1:
    new.append(i)
    print(new)


#Filter
#Global
#Local

