# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
list1 = list(map(int,input().split()))

import statistics
# print(statistics.mean(list1))
# print(statistics.median(list1))
# print(statistics.mode(list1))

mean = sum(list1)/n
mid = n/2
list1.sort()
median = (list1[int(mid)-1] + list1[int(mid)+1]) /2
print(mean)
# print(median)
print(statistics.median(list1))
print(statistics.mode(list1))
