
def sockMerchant(n, ar):
    # Write your code here
    count = 0
    for i in set(ar):
        count += ar.count(i) // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
