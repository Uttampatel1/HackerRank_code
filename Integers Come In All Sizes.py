# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# print a^b + c^d

print(a**b+c**d)

# Input (stdin)
# 9
# 29
# 7
# 27

# Expected Output
# 4710194409608608369201743232

# This result is bigger than 2^63 - 1 . Hence, it won't fit in the long long int of C++ or a 64-bit integer.