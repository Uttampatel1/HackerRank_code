# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
n = int(input())

for i in range(n):
    string = input().split()
    
    if string[0] == 'append':
        d.append(int(string[1]))
    elif string[0] == 'appendleft':
        d.appendleft(int(string[1]))
    elif string[0] == 'pop':
        d.pop()
    elif string[0] == 'popleft':
        d.popleft()
for i in d:
    print(i,end=' ')