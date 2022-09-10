# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
n = list(map(int,input().split()))
num_in = int(input())
co = Counter(n)
# print(co.items())
price = 0
for i in range(num_in):
    num = list(map(int,input().split()))
    if co[num[0]] != 0:
        price += num[1]
        co[num[0]] = co[num[0]] - 1
    # print(co.items())
print(price)
    
# Input (stdin)

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Expected Output

# 200
