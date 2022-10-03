import math

def cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

max_weight = int(input())
n_boxes = int(input())
mean = int(input())
std = int(input())

print(round(cdf(max_weight, n_boxes * mean, (n_boxes ** 0.5) * std), 4))


