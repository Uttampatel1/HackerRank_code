#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    count = 0
    max_count = 0
    max_type = 0
    for i in range(len(arr)):
        if i == 0:
            count += 1
        elif arr[i] == arr[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_type = arr[i-1]
            count = 1

    if count > max_count:
        max_count = count
        max_type = arr[i-1]

    return max_type 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
