def read_file(filename, chats):
	with open (filename, 'r', encoding='utf-8-sig') as f:
		person = None
		for line in f:
			if 'Allen' in line:
				person = 'Allen'
				continue
			elif 'Tom' in line:
				person = 'Tom'
				continue
			elif person:
				chats.append([person, line.strip()])
		return chats

def write_file(filename, chats):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for chat in chats:
			f.write(chat[0] + ': ' + chat[1] + '\n')



def main():
	chats = []
	chats = read_file('input.txt', chats)
	print(chats)
	write_file('output.txt', chats)

main()