#Regular Expression :-
"""RegEx Is  A Sequence of charcter that define search pattern
for string searching , matching validation and manipulation."""
import re

import re

#Library ---# Package/Module ---# Files

Text = ("Hello Candy")
Result = re.search("Candy" , Text)
print(Result)
if "Candy" in Text:
    print(Text, "Is Available")
else:
    print("Not In Your Life")


# Finding How MAny TIme Candy Repeated
Rx = ("I Know Nothing About Candy, But I LIke CAndy, Coz Candy Likes me")
Cx = re.findall("Candy", Rx)
print(Cx)

text3 = "Medha Is a Famous Actress"
#REplace The medha To MEdha shankar
result1 = re.sub("Medha","Medha_Shankar", text3)
print(result1)

#Split the Text At Each And Every Space
Cn = re.split("a",text3)
print(Cn)


"""
^      → Start of string
$      → End of string
.      → Any character (except newline)

\d     → Digit (0–9)
\D     → Not a digit
\w     → Word character (a-z, A-Z, 0-9, _)
\W     → Not a word character
\s     → Whitespace
\S     → Not whitespace

[abc]  → a or b or c
[a-z]  → Lowercase letters
[A-Z]  → Uppercase letters
[0-9]  → Digits
[^abc] → NOT a, b, or c

*      → 0 or more times
+      → 1 or more times
?      → 0 or 1 time (optional)
{n}    → Exactly n times
{n,}   → At least n times
{n,m}  → Between n and m times

|      → OR

()     → Capture group
(?: )  → Non-capture group
(?P<name>) → Named capture group

\b     → Word boundary
\B     → Not a word boundary

\      → Escape character
\.     → Literal dot
\$     → Literal dollar sign
\^     → Literal caret
\\     → Literal backslash

(?=...)  → Positive lookahead
(?!...)  → Negative lookahead
(?<=...) → Positive lookbehind
(?<!...) → Negative lookbehind
"""

text4 = "The cost is $999"

x = re.search(r"\$(\d+)", text4)
print(x.group(1))

#Extract the emails from the above list and print in a list
text5 = "Email: Rixz@gmail.com, Rox@gmail.com"
emails = re.findall(r"[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z]+", text5)
print(emails)

#VALIDATE A EMAIL:-
pattern = r'^\w+@\w+\.\w+$'
email = "rix@gmail.com"

if re.fullmatch(pattern, email):
    print("yes valid email")
else:
    print("invalid email")





# LoginREgistration PAge ny Using File_Handling And Resular Expression --- PRoject


