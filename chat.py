
def read_file():
	lines = []
	with open('input.txt', 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Alln'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f: 
		for line in lines:
			f.write(line + '\n')

def main(): 
	lines = read_file()
	lines = convert(lines)
	write_file('output.txt', lines)

main()
