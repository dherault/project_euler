import math

print('___')

def d(x):
	s = 0
	for i in range(1, math.ceil(x / 2) + 1):
		if x % i == 0:
			s += i

	return s

x_to_y = {}
# y_to_x = {}
amicable_numbers = set()
n = 10000
r = range(1, n)

for x in r:
	y = d(x)
	x_to_y[x] = y
	# y_to_x[y] = x

for x in r:
	y = x_to_y[x]
	if y <= n and x_to_y[y] == x and x != y:
		amicable_numbers.add(x)
		amicable_numbers.add(y)

# print(x_to_y)
# print(amicable_numbers)
print(sum(amicable_numbers))
