# Task:
# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:

# && → and
# || → or
# Both && and || should have a space " " on both sides.


# code

import re

n = int(input())
for i in range(n):
    s = input()
    s = re.sub(r'(?<= )(&&)(?= )', 'and', s)
    s = re.sub(r'(?<= )(\|\|)(?= )', 'or', s)
    print(s)
