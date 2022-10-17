from collections import Counter


S = input()
str1 = dict(Counter(S))
sorted1 = dict(sorted(str1.items(), key = lambda x: x[1], reverse = True))

for inx,i in enumerate(sorted1):
    if inx == 3:
        break
    print(i, sorted1[i])
 

# solution 2

# class OrderedCounter(Counter):
#     pass

# if __name__ == '__main__':
#     [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]



# solution 3
# d = {}
# for c in S:
#     if c in d:
#         d[c] += 1
#     else:
#         d[c] = 1
        
# data = [[d[c],c] for c in d.keys()]
# data.sort(key = lambda e: [-e[0],e[1]])

# for x in range(3):
#     print (data[x][1], data[x][0])