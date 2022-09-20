

ed,em,ey = map(int,input().split())
d,m,y = map(int,input().split())

z=0
if y < ey:
    z = 10000
elif y == ey:
    if m < em:
        z = 500*(em-m)
    elif d < ed:
        z = 15*(ed-d)

print(z)