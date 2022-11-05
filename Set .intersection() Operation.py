# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
s1 = set(map(int,input().split()))
input()
s2 = set(map(int,input().split()))

print(len(s1.intersection(s2)))