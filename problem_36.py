def base_10_to_2(n):
	x = n
	i = 0
	base_2 = ''
	
	while x > 0:
		rem = x % 2
		x = x // 2
		base_2 = str(rem) + base_2
		
	return base_2
	
def is_palindromic(n):
	t = str(n)
	l = len(t)
	il = int(l / 2)
	offset = 0 if l % 2 == 0 else 1
	
	return t[:il] == t[il + offset:][::-1]

s = 0

for x in range(1000000):
	
	if is_palindromic(x) and is_palindromic(base_10_to_2(x)):
		s += x
		
print(s)
