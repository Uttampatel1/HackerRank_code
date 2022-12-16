# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7 ,8  or 9.

import re

def validate_phone_number(number):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return pattern.match(number)

n = int(input())
for _ in range(n):
    number = input()
    if validate_phone_number(number):
        print('YES')
    else:
        print('NO')