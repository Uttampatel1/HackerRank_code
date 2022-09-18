# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

ordered_dictionary = OrderedDict()

n = int(input())

for i in range(n):
    item_name ,space, net_price = input().rpartition(' ')
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name,0) + int(net_price)
    
for item, quantity in ordered_dictionary.items():
    print(item,quantity)
    