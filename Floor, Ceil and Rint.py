import numpy as np

np.set_printoptions(legacy='1.13')

a = np.array(list(map(float,input().split())))

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

# Input (stdin)
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

# Output
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]