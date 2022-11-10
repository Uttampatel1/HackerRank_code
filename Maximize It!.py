
from itertools import product

# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))

# results = map(lambda x:sum(i**2 for i in x)%M,product(*N))

# # print (type(results))
# print(max(results))

# # Input (stdin)
# # 3 1000
# # 2 5 4
# # 3 7 8 9
# # 5 5 7 8 9 10

# # Output (stdout)
# # 206

a = [1,3,4,5]
b = [2,5,8]
print(list(product(*a)))