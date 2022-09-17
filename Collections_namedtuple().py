# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# print (dot_product)

from collections import namedtuple
N = int(input())
headers = input()
student = namedtuple('Student',headers)
students = []
for i in range(N):
    students.append(student(*input().split()))
print (sum(list(map(lambda x: float(x.MARKS),students)))/len(students))

# N, headers, total = int(input()), list(input().split()), 0
# for _ in range(N):
#     total += int(list(input().split())[headers.index('MARKS')])
# print(total/N)

