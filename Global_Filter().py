#What Are Global ()
"""Global Is  Created Outside,
#  A Function And Can Use AnyWhere"""
# from builtins import function

# What Are Local().
"""Created Inside a Function,
Only Can Use onThat Function"""


x = 10   # global variable

def demo():
    y = 5   # local variable
    print(y)

demo()
print(x)
# print(y)  can't run it coz Its a local Variable Only can be,
# run inside the function where it declared.



#Question To Ask:-
# What Happend When We Assign SAme Variable In Local And Global Both.
x = 100

def change():
    x = 500
    print(x)

change()
print(x)

#Which OutPut We Get First And Why



#filter() Function:-

#Filter() Filter Elements Based On Condition.
#Works with function + iterable
# filter(function, iterable)


numbers = [1, 2, 3, 4, 5, 6]

def even(n):
    return n % 2 == 0

result = list(filter(even, numbers))
print(result)
