#Expect python file when we handle other files (Text,json, Csv... Etc) is known as file handling.


#Open()- Inbuilt Function To handle Other Files.

"""There Are Four Modes To Handle The Files--
#X
#W
#A
#R"""

# #X- Mode(Execution Mode)- Used To Create The File---
# f = open("Rix.txt", "x")
# print(f)
# f.close()


#W- Mode (Overwrite- Mode)-
# f =open("Rix.txt", "w")
# f.write("Hey Candy")
# f.close()

#A- Mode (Append Mode) -
# f = open("Rix.txt", "a")
# f.write("How Are You")
# f.close()

#R - Mode(Read Mode)- By default open() Is in read mode

# f = open("Rix.txt", "r")
# data = f.read()
# print(data)
# f.close()


#Pickling- Is the process of converting,a python object into bytes stream it and saving to a file.
# The Process of encrytion and decreption is also known as pickling
import pickle

# data = [10, 20, 30, 40, 50]
#
# with open("Candy.txt", "wb") as f:
#     pickle.dump(data, f)
#
# print("Dumped Data")


# Deserialization:-
import pickle

with open("Candy.txt", "rb") as f:
    data = pickle.load(f)

print(data)
