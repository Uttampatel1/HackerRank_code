# Enter your code here. Read input from STDIN. Print output to STDOUT

n  = int(input())
st = []

for i in range(n):
    st.append(input())

for i in st:
    ev = ''
    od = ''
    for inx,j in enumerate(i):
        if (inx == 0 or (inx%2 ==0)):
            ev += j
        else:
            od += j
    print(ev,od)
        
