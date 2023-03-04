def bonAppetit(bill, k, b):
    # Write your code here
    bill.pop(k)
    if sum(bill)/2 == b:
        print('Bon Appetit')
    else:
        print(int(b - sum(bill)/2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
