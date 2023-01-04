
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        for j  in range(1,n+1):
            if j <= n-i:
                print(" ",end="")
            else:
                print("#",end="")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

# Input
# 6

# Your Output
#      #
#     ##
#    ###
#   ####
#  #####
# ######