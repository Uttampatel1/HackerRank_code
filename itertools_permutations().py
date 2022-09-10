
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

input1 = input().split()
string1 = list(input1[0])
# print(input1)
# print(string1)
l = list(permutations(string1,int(input1[1])))
# print(l)
l = list(map(lambda x: ''.join(x),l))
l.sort()
# print(l)
for i in l:
    print(i)

# s,n = input().split()
# print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

# Input (stdin)

# HACK 2

# Expected Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH