from statistics import mean
def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean1 = mean(arr)
    sum =0
    for i in arr:
        sum += (i-mean1)**2
        
    std = (sum/len(arr))**(1/2)
    print(std)
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
