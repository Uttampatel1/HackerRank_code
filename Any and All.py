
N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))

# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.

# Hence, the output is True.

# Can you solve this challenge in 3 lines of code or less?
# There is no penalty for solutions that are correct but have more than 3 lines.


# Input (stdin)
# 5
# 12 9 61 5 14

# Expected Output
# True