from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

# n = int(input().strip())
# counter = {}
# words = []
# for i in range(n):
#   word = input()
#   if word in counter:
#     counter[word] += 1
#   else:
#     counter[word] = 1
#     words.append(word)
    
# print(len(words))
# print(' '.join([str(counter[word]) for word in words]))