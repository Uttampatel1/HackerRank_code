# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
e = set(map(int,input().split()))
input()
f = set(map(int,input().split()))

print(len(e.symmetric_difference(f)))

# Input (stdin)

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Output

# 8