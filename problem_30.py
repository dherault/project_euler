print('___')
answers = []

for i in range(2, 10000000):
	s = 0
	for k in str(i):
		s += int(k) ** 5
		
	if i == s:
		answers.append(i)
		
print(answers, sum(answers))
