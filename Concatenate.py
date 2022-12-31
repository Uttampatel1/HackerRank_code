import numpy as np

n , m ,p = map(int,input().split())
print(np.concatenate((np.array([input().split() for _ in range(n)],int),np.array([input().split() for _ in range(m)],int)),axis=0))

# a = np.array([input().split() for _ in range(n)],int)
# b = np.array([input().split() for _ in range(m)],int)
# print(np.concatenate((a,b),axis=0))
