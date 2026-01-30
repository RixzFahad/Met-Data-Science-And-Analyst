
"""Interview Question's"""


#What Problem List comprehension Solve-?
"""It's Provide a Shorter cleaner And faster way to create
 list from iterables compared to traditional Loop"""

# Convert This List into Comprehension list
result = []
for i in range(10):
    if i%2==0:
        result.append(i*i)
print(result)

result = [i*i for i in range(10) if i % 2 == 0]
print(result)


#can list comprehension replace nested loop
pairs = [(i, j) for i in [1,2] for j in [3,4]]
print(pairs)
"""Yes List Comprehension Can Replace the Nested Loop"""



