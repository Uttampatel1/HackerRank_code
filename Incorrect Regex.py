# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)


# n=int(input())
# for i in range(n):
#     string = input()
#     try:    
#         x = re.findall(string,"hellow word")
#         print(True)
#     except:
#         print(False)

