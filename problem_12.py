import math

c = 0
triangular = 0
n = 0

def count_divisors(x):
    k = 2 # incorrect for x = 1

    for i in range(2, math.ceil(x / 2) + 1):
        if x % i == 0:
            k += 1

    return k

while n < 500:
    c += 1
    triangular += c
    n = count_divisors(triangular)

    print(triangular, n)
    pass
