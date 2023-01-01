# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

a = np.array(list(map(int,input().split())))
b = np.array(list(map(int,input().split())))

print(np.inner(a,b))
print(np.outer(a,b))