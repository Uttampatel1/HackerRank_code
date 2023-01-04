#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    p , ne , z = 0,0,0
    for i in arr:
        if i == 0:
            z +=1
        elif i > 0:
            p += 1
        elif i < 0:
            ne +=1
    print(p/n)
    print(ne/n)
    print(z/n)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# Input
# 6
# -4 3 -9 0 4 1

# Your Output
# 0.5
# 0.3333333333333333
# 0.16666666666666666