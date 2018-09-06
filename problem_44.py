import math

print('___')

def p(n):
    return n * (3 * n - 1) / 2


pentagonal_numbers = []

for i in range(1, 300):
    pentagonal_numbers.append(p(i))

print(pentagonal_numbers)

minD = math.inf

for i in pentagonal_numbers:
    for j in pentagonal_numbers:
        d = j - i
        if (d in pentagonal_numbers) and (j + i in pentagonal_numbers) and math.abs(d) < minD:
            minD = d


print(minD)
