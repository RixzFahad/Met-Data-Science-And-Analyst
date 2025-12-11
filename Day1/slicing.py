
#  egative indexing reverse a string
a = "candy"
print(a[-1:-6:-1])
print(a[-6:-1:])


# is palindrome 

a = input("Enter Your Palindrome")
rev = a[::-1]
print(rev)


palin = input("enter your word")
if palin == palin[::-1]:
    print("is Palindrome")
else:
   print("Try another word")



# Default indexing

ind = "Watashino o namaewa fahad san des"
print(len(ind))
print(ind[:10])