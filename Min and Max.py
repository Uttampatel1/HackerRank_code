import numpy as np

n, m = map(int,input().split())

arr = np.array([input().split() for _ in range(n)],int)

m = np.min(arr,axis=1)
print(np.max(m))

# Input 
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0

# Expected Output
# 3