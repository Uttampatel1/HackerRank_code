# Enter your code here. Read input from STDIN. Print output to STDOUT

# n = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# l1 = set()
# for i in range(n[1]):
#     l1.add(list(map(int,input().split())))

# def happiness(n,arr):
#     happiness = 0
#     for i in range(len(n)):
#         if n[i] in arr:
#             happiness += 1
#     return happiness
# total_hp = n[1]

# sum = 0
# for i in (l1):
#     sum += happiness(i,arr)

# h = int(sum/total_hp)
# # print(total_hp)
# # print(h)
# print(total_hp-h)

n = list(map(int,input().split()))
arr = list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

counter = 0
for i in arr:
    if i in A:
        counter += 1
    elif i in B:
        counter -= 1

print (counter)

# Sample Input
# 3 2
# 1 5 3
# 3 1
# 5 7

# Sample Output
# 1