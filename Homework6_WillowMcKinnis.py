import number_program_input as n


def secretcode(inp):
	accum = ""
	for x in inp:
		accum += str(ord(x)) + " " #add the ord()of each character in the input to the accumulator)
	return(accum)

def conjugate(inp):
	output = inp
	if (inp[-1] == "t" and inp[-2] == "i"):
		output += "t" #handle "it -> itting" cases (such as sit -> sitting)
	elif (inp[-1] == "e" and inp[-2] == "t"):
		output = output[:-1] #handle te -> ting cases (su)ch as write -> writing)
	output += "ing" # all cases add ing at the end, so do that outside the if statements to avoid the need for an 'else'
	return(output)

def convert_numbers(inp):
	accum = []
	words = inp.split(" ")
	for x in words:
		accum.append(n.word_to_number(x.lower()))
	temp = []
	hold = 0
	for x in accum:
		if x > 999:
			if hold > 0:
				temp.append(hold)
			temp.append(x)
			hold = 0
		elif hold == 0:
			hold = x
		elif x > hold:
			hold = hold*x
		else:
			temp.append(hold)
			temp.append(x)
			hold = 0
	if hold != 0:
		temp.append(hold)
	accum = temp
	temp2 = []
	hold = 0
	for x in accum:
		if x>999:
			if hold>0:
				temp2.append(hold)
			temp2.append(x)
			hold = 0
		elif hold == 0:
			hold = x
		elif x>0:
			hold = hold + x
		else:
			temp2.append(x)
			hold = 0
	if hold != 0:
		temp2.append(hold)
	accum = temp2
	temp3 = []
	for x in accum:
		if x>999:
			if hold>0:
				temp3.append(hold*x)
			else:
				temp3.append(x)
		else:
			hold = x
	if hold != 0:
		temp3.append(hold)
	accum = temp3
	final = 0
	for x in accum:
		final += x
	return(final)








choice = 2

while choice < 4 and choice > 0:
	choice = int(input("Which program would you like to run? (1 for secret code, 2 for adding -ing, 3 for converting numbers. enter any other number to quit): "))
	if choice == 1:
		print(secretcode(input("What is your input? ")))
	if choice == 2:
		print(conjugate(input("What is your input? ")))
	if choice == 3:
		print(convert_numbers(input("Your numbers: ")))
