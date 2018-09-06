import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

s = 0

for x in range(2, 2000000):
    if is_prime(x):
        s += x

print(s)
