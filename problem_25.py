print('___')

items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l = len(items)
prev_permutations = set()
permutations = set()

prev_permutations.add(items[l - 1])

print([k for k in range(l - 2, -1, -1)])

for k in range(l - 2, -1, -1):
	item = items[k]

	for permutation in prev_permutations:
		length = len(permutation)

		for i in range(length + 1):
			permutations.add(permutation[0:i] + item + permutation[i:length])

	prev_permutations = permutations
	permutations = set()

lexicographic_permutations = sorted(prev_permutations)

print(lexicographic_permutations[999999])
