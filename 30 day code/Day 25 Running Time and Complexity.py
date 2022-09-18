# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

n = int(input())

def isPrime(num):
    
    for i in range(2,int(sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

for _ in range(n):
    
    num = int(input())
    
    if num >=2 and isPrime(num):
        print("Prime")
    else:
        print("Not prime")

