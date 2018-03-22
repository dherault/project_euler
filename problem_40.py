print('___')

t = ''
k = 0

def unqueue():
	global t
	global k
	
	if len(t) == 0:
		k += 1
		t += str(k)
	
	x = t[0]
	t = t[1:]
	
	return x


stops = [1, 10, 100, 1000, 10000, 100000, 1000000]
product = 1

for x in range(1, 1000001):
	n = unqueue()
	
	if x in stops:
		print(x, n)
		product *= int(n)
		
print(product)

