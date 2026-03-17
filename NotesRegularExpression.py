"""
Regular Expressions or RegEx are special string texts that help us identify patterns in data.
To use RegEx we need to import the re module
After importing it we can use it to find and detect different patterns in certain data
"""

import re

"""
The are different methods with the re module and we are going to go through each one
"""
# re.match()
# This method searches the beginning of the string and returns the objects that match it else returns None
# ONLY CHECKS FROM BEGINNING
#eg

txt = 'I love to teach python and javaScript'
# it returns an object with span and match
match = re.match('I will love to teach', txt, re.I)
# re.match(substring, string, re.I)
# Substring is a string or pattern, string is the text we look for a pattern, re.I is case ignore
# Lets say the substring was 'I will love to teach' It will only stop on 'I' because its at the BEGINNING
# Or if it was 'Jason I love' it will return None
print(match)