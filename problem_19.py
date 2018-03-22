print('___')

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_days_in_month(y, m):
	if m != 2:
		return days_in_month[m - 1]
	
	if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
		return 29
		
	return 28
	
s = 0
day = 0

for y in range(1900, 2001):
	for m in range(1, 13):
		for d in range(1, get_days_in_month(y, m) + 1):
			day += 1
			
			if day == 7:
				day = 0
				
			if y > 1900 and day == 0 and d == 1:
				s += 1
		
print(s)
