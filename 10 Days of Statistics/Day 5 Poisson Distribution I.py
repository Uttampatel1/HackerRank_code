# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial, exp

miu = float(input())
x = int(input())
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" %poisson_prob)

# lm = 2.5
# k = 5
# e = 2.71828

# def fact(n):
#     return 1 if n == 0 else n*fact(n-1)

# p = ((lm**k)*(e**(-lm)))/fact(k)

# print(p)

