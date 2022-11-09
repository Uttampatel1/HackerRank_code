# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

r = int(input())
lt = list(map(int,input().split()))

k = Counter(lt)

d = dict(k)

print(min(d, key=lambda k:d[k]))