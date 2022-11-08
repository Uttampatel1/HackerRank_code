# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))

# input()
# l = set(map(int,input().split()))
# n = int(input())

# for i in range(n):
#     s = input().split()
#     st = s[0]
#     if st == "intersection_update":
#        num = set(map(int,input().split()))
#        l.intersection_update(num) 
#     elif st == "difference_update":
#         num = set(map(int,input().split()))
#         l.difference_update(num)
        
#     elif st == "symmetric_difference_update":
#         num = set(map(int,input().split()))
#         l.symmetric_difference_update(num) 
        
#     elif st == "update":
#         num = set(map(int,input().split()))
#         l.update(num) 
# print(sum(l))

# Input (stdin)

# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

# Expected Output

# 38