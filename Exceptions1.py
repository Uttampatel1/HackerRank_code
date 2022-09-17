# Enter your code here. Read input from STDIN. Print output to STDOUT
def div(a,b):
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e :
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)
n = int(input())
for i in range(n):
    a,b = input().split()
    div(a,b)

# for i in range(int(input())):
#     try:
#         a,b=map(int,input().split())
#         print(a//b)
#     except Exception as e:
#         print("Error Code:",e)