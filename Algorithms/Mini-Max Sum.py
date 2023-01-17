
def miniMaxSum(arr):
    # Write your code here
    max1 = max(arr)
    min1 = min(arr)
    print(sum(arr)-max1,sum(arr)-min1)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
