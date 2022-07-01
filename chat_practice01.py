def read_file(filename, chats):
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chats.append(line.strip())
		return chats

def convert(chats, new):
	person = None
	for line in chats:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, new):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in new:
			f.write(line + '\n')

def main():
	chats = []
	chats = read_file('input.txt', chats)
	print(chats)
	new = []
	new = convert(chats, new)
	print(new)
	write_file('output.txt', new)

main()