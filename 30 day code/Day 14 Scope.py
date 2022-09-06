class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    
    # def computeDifference(self):
    #     ar = []
    #     for i in self.__elements:
    #         for j in self.__elements:
    #              ar.append(abs(i-j))
        
    #     self.maximumDifference = max(ar)
        
    def computeDifference(self):
        x = 101
        y = 0

        for item in self.__elements:
            if item < x:
                x = item
            if item > y:
                y = item
        self.maximumDifference = y - x
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


# Input (stdin):

# 3
# 1 2 5

# Output:

# 4