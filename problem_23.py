import math

print('___')

def d(x):
	s = 0
	for i in range(1, math.ceil(x / 2) + 1):
		if x % i == 0:
			s += i
	
	return s

n = 28123
r = range(1, n + 1)
abudent_numbers = set()

for x in r:
	if d(x) > x:
		abudent_numbers.add(x)
		
# print(abudent_numbers)

sumables = set()

for x in r:
	sumable = True
	for y in abudent_numbers:
		if x - y in abudent_numbers:
			sumable = False
			break
	
	if sumable:
		sumables.add(x)

print(sum(sumables))
 
