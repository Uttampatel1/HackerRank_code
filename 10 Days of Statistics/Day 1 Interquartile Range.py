# from statistics import median
# def interQuartile(values, freqs):
#     # Print your answer to 1 decimal place within this function
#     s = []
#     n = len(values)
#     for i in range(len(values)):
#         for j in range(freqs[i]):
#             s.append(values[i])
#     s = sorted(s)
#     q1 = median(s[:n//2])
#     q3 = median(s[(n+1)//2:])
#     print(q3-q1)
    

# if __name__ == '__main__':
#     n = int(input().strip())

#     val = list(map(int, input().rstrip().split()))

#     freq = list(map(int, input().rstrip().split()))

#     interQuartile(val, freq)


import statistics as st

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if n%2 != 0:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2+1:])
else:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])

ir = round(float(q3-q1), 1)
print(ir)
