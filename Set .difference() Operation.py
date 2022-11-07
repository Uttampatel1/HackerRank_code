# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
e = set(map(int,input().split()))
input()
f = set(map(int,input().split()))

print(len(e.difference(f)))