import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for n in range(N)])
print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(numpy.round(numpy.std(A), 11))

# Input
# 2 2
# 1 2
# 3 4

# Your Output 

# [1.5 3.5]
# [1. 1.]
# 1.11803398875