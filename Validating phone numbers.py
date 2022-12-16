# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7 ,8  or 9.

import re

n = int(input())
for i in range(n):
    s = input()
    if re.match(r'[789]\d{9}$', s):
        print('YES')
    else:
        print('NO')