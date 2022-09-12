if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps = 0
    for i in range(n-1):
        for j in range(n-1):
            if (a[j] > a[i]):
                a[i] , a[j] = a[j] , a[i]
                numberOfSwaps += 1
        if numberOfSwaps == 0:
            break
    print(a)
    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])


# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# nofswap = 0
# for i in range(0,n-1):
#     for i in range(0,n-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
#             nofswap +=1

# print("Array is sorted in", nofswap, "swaps.")
# print("First Element:",a[0])
# print("Last Element:",a[-1])