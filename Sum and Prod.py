import numpy as np

n, m = map(int,input().split())

arr = np.array([input().split() for _ in range(n)],int)

s = np.sum(arr,axis=0)
print(np.prod(s))

# Input (stdin)
# 2 2
# 1 2
# 3 4

# Output
# 24