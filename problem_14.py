import math

memory = { 1: 1 }

def iterate(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def count_chain(n):
    if n in memory:
        return memory[n]

    count = 1 + count_chain(iterate(n))

    memory[n] = count

    return count

maxi = 0
index = 0

for i in range(1, 1000000):
    print(i)
    count = count_chain(i)

    if count > maxi:
        maxi = count
        index = i

print(maxi, index)
