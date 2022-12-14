# A valid email address meets the following criteria:

# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is 1,2 , or3  characters in length.
# Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

import re

def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', s)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        name, email = input().split()
        if fun(email):
            print(name, email)



