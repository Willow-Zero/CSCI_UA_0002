def forcetoint(num):
	while type(num) != int:
		try:
			num = int(num)
		except:
			num = input("ERROR(NaN):Please input again: ")
	return(num)

def sortarray(input):
	i = 0
	while i == 0:
		i = 1
		for x in range(len(input)-1):
			if input[x]>input[x+1]:
				input[x],input[x+1] = input[x+1],input[x]
				i = 0
	return(input)
def problem1():
	many = input("How many integers? ")
	many = forcetoint(many)
	lowest = input("What is the lowest integer? ")
	lowest = forcetoint(lowest)
	highest = input("What is the highest integer? ")
	highest = forcetoint(highest)
	while lowest >= highest:
		print("ERROR:INVALID RANGE")
		lowest = forcetoint(input("What is the lowest integer? "))
		highest = forcetoint(input("What is the highest integer? "))
	numbers = []
	i = 0
	while i<many:
		innn = input("Next Integer: ")
		innn = forcetoint(innn)
		inta = 0
		while innn > highest or innn < lowest:
			innn = input("ERROR: out of range: ")
			innn = forcetoint(innn)
		numbers.append(innn)
		i += 1 
	print(numbers)

def problem2():
    filename = input("What is the file name? ")
    f = open(filename,"r")
    lines = f.readlines()
    vowellist = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for line in lines:
        line = line.lower()
        print(line)
        for char in line:
            if char in vowellist:
                vowellist[char] += 1
    open(filename + ".vowel_profile","w").write("")
    w = open(filename+".vowel_profile","a")
    w.write("This is a Vowel Profile file.")
    w.write("\nA Frequency: " + str(vowellist["a"]))
    w.write("\nE Frequency: " + str(vowellist["e"]))
    w.write("\nI Frequency: " + str(vowellist["i"]))
    w.write("\nO Frequency: " + str(vowellist["o"]))
    w.write("\nU Frequency: " + str(vowellist["u"]))
    print(vowellist)
	
	
	
def switch(list,p1,p2):
	list[p1],list[p2] = list[p2],list[p1]
	return list


def sort(unsort):
	sorted = False
	while sorted == False:
		i = 0
		sorted = True
		for x in range(len(unsort)-1):
			if unsort[i][4] > unsort[i+1][4]:
				switch(unsort,i,i+1)
				sorted = False
			i+=1
	return(unsort)

def problem3():
	file = input("File name: ")
	infile = open(file,"r").readlines()
	out = []
	for team in infile:
		team = team.replace("\n","").rsplit("	")
		print(team)
		team[1],team[2],team[3] = int(team[1]),int(team[2]),int(team[3])
		score = team[1]+ (team[2]/2)
		print(team[0] + ", " + str(score))
		out.append([team[0],team[1],team[2],team[3],score])
	open(file + ".out","w").write("")
	sorted = sort(out)
	for x in sort(out):
		for y in x:
			open(file + ".out","a").write(str(y))
			open(file + ".out","a").write("	")
		open(file + ".out","a").write("\n")
def problem4():
	max_stars = input("What is the maximum star score? ")
	max_stars = forcetoint(max_stars)
	intsv = input("What is the name of the tsv file (exclude '.tsv')? ")
	try:
		datalines = open(intsv+".tsv","r").readlines()
	except:
		print("ERROR: NO SUCH FILE")
		exit()
	i = 0
	for line in datalines:
		line = line.replace("\n","").rsplit("\t")
		datalines[i] = line
		i += 1
	print(datalines)
	for line in datalines:
		if len(line) != len(datalines[0]):
			print("ERROR: INPUT FILE INVALID")
			exit()
	problem4pt2(max_stars,datalines,intsv)

def problem4pt2(max_stars,datalines,intsv):
	newline = []
	for x in datalines[0]:
		if x == "Customer Number":
			cusnum = input("What is the customer number? ")
			cusnum = forcetoint(cusnum)
			newline.append(cusnum)
		else:
			rating = input("What is your rating out of " + str(max_stars) + " stars of " + x +"? ")
			rating = forcetoint(rating)
			while rating > max_stars or rating < 1:
				rating = forcetoint(input("ERROR:OUT OF RANGE: "))
			newline.append(rating)
	datalines.append(newline)
	if input("Do you want to add another value? (y/n) ") == "y":
		problem4pt2(max_stars,datalines,intsv)
	else:
		open(intsv+".tsv","w").write("")
		for x in datalines:
			for y in range(len(x)):
				open(intsv+".tsv","a").write(str(x[y]))
				if y != len(x)-1:
					open(intsv+".tsv","a").write("\t")
			open(intsv+".tsv","a").write("\n")
		averagefield = []
		for x in datalines[0]:
			averagefield.append(0)
		for x in range(len(datalines)-1):
			i = 0
			for y in range(len(datalines[0])):
				averagefield[i] += float(datalines[x+1][y])
				i += 1
		for x in range(len(averagefield)):
			averagefield[x] = averagefield[x]/(len(datalines)-1)
		for x in range(len(averagefield)):
			if x != 0:
				print("average rating of " + datalines[0][x] + " is " + str(averagefield[x]))


run = input("Which program would you like to run?(1-4) ")
if run == "1":
	problem1()
if run == "2":
	problem2()
if run == "3":
	problem3()
if run == "4":
	problem4()
