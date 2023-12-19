"""

https://www.w3schools.com/python/python_regex.asp

Python has a built-in package called re, which can be used to work with Regular Expressions.
import re

findall	- Returns a list containing all matches
search	- Returns a Match object if there is a match anywhere in the string

"""

import re

text = "hello world!"

# []	A set of characters
# Find all lower case characters alphabetically between "a" and "m":

list_of_results = re.findall("[a-m]", text)
print(list_of_results)

#############################################

# \	Signals a special sequence (can also be used to escape special characters)

text = "hello my 56 friends! I have 500 dollar with me"

list_of_results = re.findall("\d", text)
print(list_of_results)

#############################################

text = "hello my? 56 friends! I have 500 dollar with me"
result = re.findall('friends(,?.*)', text)
result = re.findall('hello\\W+(\\w+)', text)
print(result)