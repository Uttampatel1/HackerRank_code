# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print (i)

# print(d.keys())
# print(d.values())

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import defaultdict
# d = defaultdict(list)

# l = list(map(int,input().split()))
# n , m = l[0],l[1]

# for i in range(n):
#     d["A"].append(input())
# for i in range(m):
#     d["B"].append(input())

# for i in range(m):   
#     if d["B"][i] in d["A"]:
#         for inx,i in enumerate(d["A"]):
#             if i == d["B"][i]:
#                 print(inx+1,end=" ")
#         print("")
#     else:
#         print(-1)

from collections import defaultdict
d = defaultdict(list)
list1=[]
n, m = map(int,input().split())
for i in range(1, n+1):
    d[input()].append(str(i))


for i in range(m):
    b = input()
    if b in d: print(' '.join(d[b]))
    else: print(-1)
    