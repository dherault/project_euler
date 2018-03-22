import math

print('___')

s = 0

for x in range(10, 1000000):
	fs = 0
	for char in str(x):
		fs += math.factorial(int(char))
		
	if fs == x:
		s += x
		
print(s)
