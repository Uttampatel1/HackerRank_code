from itertools import combinations

input()
s = input().split()
k = int(input())

c = list(combinations(s, k))
f = filter(lambda c: 'a' in c, c)
print("{0:.3}".format(len(list(f))/len(c)))






