import math

print('___')

n = 1001
center = math.floor(n / 2)
grid = []
x = 1
pos = (center, center)

for i in range(n):
	grid.append([0] * n)


direction_index = -1
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

moves = []
offset = 1
jump = False
over = False

while not over:
	direction_index += 1

	if direction_index == 4:
		direction_index = 0

	direction = directions[direction_index]


	if offset == n:
		over = True
		offset -= 1

	moves.append((offset, direction))

	if jump:
		offset += 1
		jump = False
	else:
		jump = True

grid[pos[1]][pos[0]] = x

while len(moves):
	offset, direction = moves.pop(0)

	for i in range(1, offset + 1):
		pos = (pos[0] + direction[0], pos[1] + direction[1])

		x += 1
		grid[pos[1]][pos[0]] = x

s = -grid[center][center]

for i in range(n):
	s += grid[i][i] + grid[n - i - 1][i]

print(s)
