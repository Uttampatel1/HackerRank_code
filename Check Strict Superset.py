def isstrictsuperset(a,b):
    # true if a is a strict superset of b
    # return b.issubset(a) and not(a.issubset(b))
    return a.issuperset(b)
    
a = set(int(x) for x in input().split(' '))
n = int(input())
res = True

for _ in range(n):
    b = set(int(x) for x in input().split(' '))
    res &= isstrictsuperset(a,b)
    
print(res)


# Input (stdin)
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# Expected Output
# False