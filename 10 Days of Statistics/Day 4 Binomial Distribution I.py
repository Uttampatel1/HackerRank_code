# Task :
# The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e., 1.234 format).

# Input Format :
# A single line containing the following values:
# 1.09 1

# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format:
# 0.656
# Print a single line denoting the answer, rounded to a scale of  decimal places


# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))    

    
def binomial(x,n,p):
    return nCr(n,x) * p**x * (1-p)**(n-x)
    

l ,r = list(map(float,input().split(" ")))
odds = 1/r
print(round(sum([binomial(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))


# arr=map(float,input().split())
# p=arr[0]/sum(arr)
# q=arr[1]/sum(arr)
# sum1=0
# for i in range(3,7):
#     temp=nCr(6,i)
#     temp1=(p**i)*(q**(6-i))
#     sum1+= temp*temp1
# print (round(sum1,3))