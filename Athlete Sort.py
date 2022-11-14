
if __name__ == '__main__':
    n, m = map(int,input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    P = sorted(arr,key=lambda row:row[k])
    for i in range(n):
        for j in range(m):
            print(P[i][j],end=" ")
        print()

# Input (stdin)
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# Your Output (stdout)
# 7 1 0 
# 10 2 5 
# 6 5 9 
# 9 9 9 
# 1 23 12 