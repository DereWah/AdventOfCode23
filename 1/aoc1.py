import re


map = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

f = open("input.txt", "r")
input = f.readlines()
f.close()

sum = 0

formatted_input = []

for i, line in enumerate(input):
	formatted_input.append(line)
	for str_int in map.keys():
		print(str_int)
		formatted_input[i] = formatted_input[i].replace(str_int, str_int[0]+str_int+str_int[len(str_int)-1])
	print(formatted_input[i] +" | "+ line)
	for str_int in map.keys():
		formatted_input[i] = (formatted_input[i].replace(str_int, str(map[str_int])))
		
for line in formatted_input:
	result = re.findall("\d{1}", line)

	sum += int(result[0])*10+int(result[len(result)-1])
	
print(sum)
