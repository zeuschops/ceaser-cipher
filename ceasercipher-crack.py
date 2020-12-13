import os

#Symbols would be supported, but the arrangement would mess with things
selectionArr = 'abcdefghijklmnopqrstuvwxyz1234567890 '

user_text = input("Cipher Text: ")
f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

for i in range(len(words)):
	words[i] = words[i].lower()

if len(words[-1]) == 0:
	del words[-1]

def single_shift(shift, text):
	to_return = ''
	for i in range(len(text)):
		position = (selectionArr.index(text[i]) + shift) % len(selectionArr)
		to_return += selectionArr[position]
	return to_return

def multi_shift(shift, text):
	to_return = ''
	for i in range(len(text)):
		position = (selectionArr.index(text[i].lower()) + (shift * i)) % len(selectionArr)
		to_return += selectionArr[position]
	return to_return

user_text = multi_shift(5, "test this thing")

#First pass is checking single-shifted ceaser ciphers
#	(char1 + shift, char2 + shift, char3 + shift, ...)
passed = False
for i in range(-len(selectionArr),len(selectionArr)):
	temp_store = single_shift(i, user_text)
	if len(temp_store.split(' ')) != 1:
		if temp_store.split(' ')[0] in words:
			passable = True
			for word in temp_store.split(' '):
				if word not in words:
					passable = False
			if passable:
				print("Shifted: ", i)
				print("Result:  ", temp_store)
				passed = True
				break

#Second pass is checking multi-shifting ceaser ciphers
#	(char1 + shift, char2 + (shift * 2), char3 + (shift * 3), ...)
if not passed:
	for i in range(-len(selectionArr),len(selectionArr)):
		temp_store = multi_shift(i, user_text)
		if len(temp_store.split(' ')) != 1:
			passable = True
			for word in temp_store.split(' '):
				if word not in words:
					passable = False
			if passable:
				print("Shifted: ", i)
				print("Result:  ", temp_store)
				passed = True
				break