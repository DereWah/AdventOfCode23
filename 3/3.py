

f = open("input.txt", "r")
lines = f.read().splitlines()

total_lines = len(lines)
total_chars = len(lines[0])

total_sum = 0

total_gear_ratio = 0

matrix = []


def check_adiacent(i, j):
	n = -1
	m = -1
	part_sum = 0
	gear_amount = 0
	gear_prod = 1
	while (n <= 1):
		while (m <= 1):
			try:
				print(f"x: {j+m} y: {i+n}")
				print(int(matrix[i+n][j+m]))
				number = char_to_number(i+n, j+m)
				part_sum += number
				
				if(matrix[i][j] == "*"):
					gear_amount += 1
					gear_prod *= number
			except:
				print("inv")
			m += 1
		n += 1
		m = -1
	if(gear_amount) == 2:
		return part_sum, gear_prod
	else:
		return part_sum, 0
			
			
def char_to_number(i, j):
	current_number = 0
	mult = 1
	valid = True
	while(valid and
		j >= 0):
		try:
			root = int(matrix[i][j])
		except Exception as e:
			valid = False
			j -= 1
			break
		j += 1
	valid = True
	
	while(valid and
		j >= 0):
		try:	
			new_number = int(matrix[i][j])
			current_number += mult*new_number
			mult *= 10
			matrix[i][j] = "."
		except Exception as e:
			valid = False
			break
		j -= 1
	if (current_number > 0):
		return current_number

for l in lines:
	matrix.append(list(l))
	
for i, line in enumerate(matrix):
	for j, char in enumerate(line):
		if(char != "."):
			try:
				int(char)
			except:
				print(matrix[i][j])
				partial_sum, partial_gear_ratio = check_adiacent(i, j)
				total_sum += partial_sum
				total_gear_ratio += partial_gear_ratio
				
print(total_sum)
		
print(total_gear_ratio)
		

