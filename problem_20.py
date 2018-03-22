def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i

    return product

s = 0
for x in str(factorial(100)):
    s += int(x)

print(s)
