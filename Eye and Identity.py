# Your task is to print an array of size N x M with its main diagonal elements as 1's and 0's everywhere else.

import numpy as np

N, M = map(int, input().split())

np.set_printoptions(legacy='1.13')
print(np.eye(N, M, k = 0))

