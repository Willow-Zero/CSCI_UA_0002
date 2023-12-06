def sortarray(input):
        i = 0
        while i == 0:
                i = 1
                for x in range(len(input)-1):
                        if input[x][0][0]>input[x+1][0][0]:
                                input[x],input[x+1] = input[x+1],input[x]
                                i = 0
        return(input)
def checkifin(search,array):
	test = 0
	for x in range(len(array)):
		if array[x][0] == search:
				test = 1
				return(x)
	if test != 1:
		return(-1)






def wordfreq():
	inputfile = open(input("what is the name of the file? "),"r")
	lines = inputfile.readlines()
	for line in range(len(lines)):
		lines[line] = lines[line].split(" ")
		for x in range(len(lines[line])):
			lines[line][x] = lines[line][x].strip(",'?!.\n)(\"").lower()
#	print(lines)
	wordlist = []
	for line in lines:
		for word in line:
			check = checkifin(word,wordlist)
	#		print(check)
			if check >= 0:
				wordlist[check][1] += 1
			else:
				wordlist.append([word,1])	
	sorted = sortarray(wordlist)
	open("wordcount.tsv","w").write("")
	for x in sorted:
		open("wordcount.tsv","a").write(x[0]+"	"+ str(x[1]) + "\n")


holidays = {"christmas":"12/25/2021","ramadan":"03/23/2021","passover":"03/27/2021","diwali":"11/03/2021","easter":"04/04/2021","valentines":"02/14/2021","juneteenth":"06/19/2021","halloween":"10/31/2021","thanksgiving":"11/25/2021"}
def holidates(instring):
	out = ""
	for x in instring.split(" "):
		if x in holidays:
			out += holidays[x]
			out += " "
		else: 
			out += x
			out += " "
	return(out)

def addnumber(book,name,number):
	if name in book:
		numlist = book[name]
		print(numlist)
		numlist.append(number)
		book[name] = numlist
		print(book[name])
	else:
		book[name] = [number]
	return(book)

def phonebook(infile):
	book = {}
	f = open(infile,"r")
	linea = f.readlines()
	for line in linea:
		line = line.strip("\n").split("\t")
		book = addnumber(book,line[0],line[1])
	i = 1
	while i == 1:
		name = input("Next Name(leave empty to save and quit): ")
		if name == "":
			i = 0
			break
		number = input("Phone Number: ")
		addnumber(book,name,number)
	open("output_"+infile,"w").write("")
	namelist = []
	for num in book:
		namelist.append(num)
	print(namelist)
	namelist.sort()
	for entry in namelist:
		for number in book[entry]:
			open("output_"+infile,"a").write(entry + "\t" + number + "\n")

def reversephonebook(infile,outfile):
	book = {}
	f = open(infile,"r")
	linea = f.readlines()
	for line in linea:
		line = line.strip("\n").split("\t")
		book = addnumber(book,line[1],line[0])
	open(outfile,"w").write("")
	numlist = []
	for num in book:
		numlist.append(num)
	numlist.sort()
	for entry in numlist:
		for number in book[entry]:
			open(outfile,"a").write(entry + "\t" + number + "\n")


program = input("Which program would you like to run(1-4)? ")
if program == "1":
	wordfreq()
if program == "2":
	print(holidates(input("String: ")).lower())
if program =="3":
	phonebook(input("Input Phonebook: "))
if program == "4":
	reversephonebook(input("Input file: "),input("Output file: "))
