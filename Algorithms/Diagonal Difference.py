# Title: Diagonal Difference

# Problem: Given a square matrix, calculate the absolute difference between the sums of its diagonals.


# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d_l , d_r = 0 ,0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j :
                d_l += arr[i][j]
    for i in range(n):
        for j in range(n):
            if (i+j) == (n-1) :
                d_r += arr[i][j]   
    return abs(d_l - d_r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Expected Output
# 15