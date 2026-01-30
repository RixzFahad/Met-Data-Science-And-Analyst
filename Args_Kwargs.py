def details(**name):
    print(name)
details(name = "Rixz", age =21 , locaation = "Hyderabad")

# print the sum of all given number's

def sum(*n1):
    print(n1)

sum(1,2,3,4,5,6,7,8,9)


#Kwargs:- Keyword arbitory arguement
"""when we dont know how many parameters need to pass"""
"""The Default data type of kwargs are Dictionary"""

#Args:- Arbiotory Arguements
"""When we dont know how many arguement need to pass we use args"""
"""Args default datatypes are tuple()"""

#Create a sum function
t = (1,2,3,4,5,5,6,7)
# print(sum(t))
total = 0



#Return :-Keyword Send back all the values to the caller
#Return is similar to the print(), when we use the return call the functio with print

def sum(*num):
    total = 0
    for i in num:
        total = total + i
    return(total)


print(sum(69,69,69))




#Coding Question

# Write a function that return the greator number from 2 number's.
a = 15
b = 254
# if a > b:
#     print(a)
# else:
#     print(b)
def maxium(a,b):
    if a > b:
        return a
    else:
        return b


# Write a function to print the length of A string.
def string_length(s):
    return len(s)

print(string_length("Rixz"))

# write a function to calculate the factorial of a number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(factorial(5))



#what is function?
"""A Function is a block of code runs whe we call it"""
#How can we create a function --> def
"""def function_name(parameters):
    # function body
    return value   # optional"""
#what is a parameter(variable) and arguments(values)?
"""Parameter is a variable in a function definition,
 while an argument is the actual value passed to 
 that function during the function call."""
#what is default function?(by default assign a value to parameter)
"""def greet(name="User"):
    print("Hello", name)

greet("Rixz")   # Argument given
greet()         # No argument → default used
"""
#what is args and kwargs?
"""**kwargs (Arbitrary Keyword Arguments)
Used to pass key-value pairs
Stored as a dictionary
Accessed using .items()"""
#what is the default data types for ARGS and KWARGS?
"""The default data type of *args is tuple, and the default data type of **kwargs is dictionary.
If you want, I can give you 1-line notes, mock interview questions, or coding challenges next 🚀"""
#What is return keyword?
"""The return keyword is used to send a value from,
 a function back to the caller and terminate the function execution."""
#How many arguments and parameters can we create?
"""In Python, there is no predefined limit on the number of parameters or arguments.
 Using *args and **kwargs, 
 we can pass an unlimited number of positional and keyword arguments."""



