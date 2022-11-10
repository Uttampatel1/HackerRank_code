# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    x , a ,y ,b =  input(),set(map(int,input().split())),input(),set(map(int,input().split()))
    print(a.issubset(b))


# Input (stdin)
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Expected Output
# True
# False
# False