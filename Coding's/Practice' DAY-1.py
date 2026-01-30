#Write a function that prints numbers from 1 to N.
def print_number(n):
 for i in range(1,n+1):
     print(i)

print_number(10)

""" For PrintIng Numbers in Reverse Form"""

def rev_print_number(n):
    for i in range(n, 0, -1):
        print(i)

rev_print_number(10)


# Q2. Check if a number is even or odd

def odd_even(n):
    if n%2==0:
        print("Your Number Is Even")
    else:
        print("Your Number Is Odd")
odd_even(68.69)


#2nd Approach

def odd_Eve(n):
    if not isinstance(n,int):
        print("Please Enter an Interger")
        return
    if n%2==0:
        print("Your Number Is Even")
    else:
        print("Your Number Is Odd")

odd_Eve(68.69)
"""WE Can Also Change the data type into Int that the variable is change from flaot and if ther
Is any 67.22 Number it Return Odd Not Show Even By taking the last digits"""


odd_even(68.69)


# 🔹 Q3. Sum of all elements in a list
def sum_num(Rixx):
    count = 0
    for num in Rixx:
        count += num
    return count
print(sum_num([22,33,44,55]))

# 🔹 Q4. Count vowels in a string

def Vow_count(V):
    vowels = "AEIOUaeiou"
    count = 0
    for character in V:
        if character in vowels:
            count += 1
    return count
print(Vow_count( "AEIOUaeiou"))


# 🔹 Q5. Reverse a string

def rev_str(st):
    return st[::-1]
print(rev_str("Candy"))
""" Palindrome """



#🔹 Q6. Find the largest number in a list
"""Don't Use Max()"""

def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return ("The Maximum Is ", maximum)
print(find_max([34,3,2,3,4,5]))


# 🔹 Q7. Remove duplicates from a list

def remove_dup(dp):
    result = []
    for num in dp:
        if num not in result:
            result.append(num)
    return result

print(remove_dup(([1, 2, 2, 3, 1])))


# 🔹 Q8. Check if a string is palindrome
def palindrome(n):
    return n == n [::-1]
print(palindrome("madam"))


#2nd Aproach

def pel_check(pel):
    if pel == pel[::-1]:
        print("The String Is Palindrome")
    else:
        print("try Another Words")
print(pel_check("CANdy"))


# 🔹 Q9. Count frequency of each element in a list

def frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

print(frequency([1, 2, 2, 3, 3, 3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]))



# 🔹 Q10. Find first non-repeating character
"""Screening Question's"""


def first_unique_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

print(first_unique_char("aazbbcddexe"))

# 🔹 Q11. Check if two strings are anagrams
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted (s1)== sorted (s2)
print(are_anagrams("listen", "silent")) # Anagram MEans They both varaible contains same charactor's in there words

print(are_anagrams("race", "care"))   # Anagram
print(are_anagrams("hello", "world")) # Not Anagram



# 🧠 Simple Explanation (Easy English)
#
# Anagram means:
# Both words contain the same characters with the same frequency,
# order does not matter.
#
# "listen" → ['l','i','s','t','e','n']
#
# "silent" → ['s','i','l','e','n','t']
#
# After sorting → both become exactly the same



"""🔹 Q12. Find missing number from 1 to N"""

def missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(missing_number([1, 2, 4, 5], 5))



"""
🔥 HOW SCREENING ROUNDS JUDGE YOU

They check:

Logic clarity

Edge cases

Clean code

Time complexity

❌ They don’t care about:

Fancy tricks

One-liners
"""