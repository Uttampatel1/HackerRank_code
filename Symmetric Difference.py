mc = int(input())
m = set(map(int,input().split()))
nc = int(input())
n = set(map(int,input().split()))

s = list(m.symmetric_difference(n))
for i in sorted(s):
    print(i)


# Sample Input:

# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}


# Sample Output :
# 5
# 9
# 11
# 12