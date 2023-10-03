#This is a digitized and slightly modified version of this(https://kokizzu.blogspot.com/2016/06/flowchart-to-choose-your-programming.html)
#flowchart for deciding which language to use.
#I have added a few languages, specifically brainfuck and Fortran

def yninput(x): #this function is used to filter and parse the input given to the program. While the program does ask the user to input only Y/N, accounting for a user who mistypes or misunderstands is best. It also cuts down on code relative to checking at every if statement.
	ini = input(x).upper()[0]
	while (ini!= "Y" and ini != "N"):
		ini = input("Invalid! Please try again: ").upper()[0]
	return(ini)
	



print("Welcome! You've decided to program something! Good luck. Please give Y/N as answers.") 
runtime = yninput("Do you really care about runtime performance? ") 
while (runtime!="Y" and runtime !="N"):#from here, its just a bunch of nested if statements. I wont annotate them, as theyre each fairly self-explanatory with the above flowchart.
	print("Invalid!")
	runtime=yninput("> ")
if (runtime=="Y"):
	maso = yninput("Are you a masochist? ")
	if (maso == "Y"):
		fort = yninput("Is your machine old enough to be the president, plus a decade or so? Or, do you have to do high-performance mathematics? ")
		if (fort == "Y"):
			print("Why are you here? Start coding in Fortran, you know its the only thing that beauty runs.")
		if (fort == "N"):
			moz = yninput("Do you like Mozilla?")
			if (moz == "Y"):
				print("Use Rust")
			if (moz == "N"):
				brain = yninput("Do you want to be able to read your code? ")
				if (brain == "Y"):
					print("Use C++")
				if (brain =="N"):
					print("Use Brainfuck, and hope nobody ever learns of your crimes.")
	if (maso =="N"):
		new = yninput("Do you want to learn something new?")
		if (new =="Y"):
			print("Use C")
		if (new=="N"):
			lines = yninput("Do you like long lines?")
			if (lines =="Y"):
				print("Use Java(")
			if (lines =="N"):
				FP=yninput("Do you like FP?")
				if (FP == "N"):
					micro = yninput("Do you like Microsoft? ")
					if (micro == "Y"):
						cp = yninput("Do you hate C++? ")
						if (cp == "N"):
							print("Use C#")
						if (cp == "Y"):
							ancient=yninput("Is your computer ancient? ")
							if (ancient=="Y"):
								print('Use VB6')
							if (ancient=="N"):
								print('Use VB.NET')
					if (micro =="N"):
						fb = yninput("Do you like Facebook/Meta? ")
						if (fb == "Y"):
							print("Use Hack. Also reevaluate your priorities.")
						if (fb == "N"):
							apple = yninput("Do you like Apple? ")
							if (apple == "Y"):
								maso2 = yninput("Are you actually a bit masochistic? ")
								if (maso2 == "Y"):
									print("Use objective-C")
								if (maso2 == "N"):
									print("Use Swift")
							if (apple=="N"):
								goog = yninput("Do you like Google? ")
								if (goog == "N"):
									print("Use Delphi or Lazarus")
								if (goog =="Y"):
									java = yninput("Do you also like Java and Javascript? ")
									if (java == "Y"):
										print("Use Dart")
									if (java == "N"):
										print("Use Go")
				if (FP =="Y"):
					maso = yninput("But really, are you a masochist? ")
					if (maso == "N"):
						print("Use Scala")
					if (maso == "Y"):
						parenthetic = yninput("Do you like parenthesis? ")
						if (parenthetic == "Y"):
							print("Use Clojure")
						if (parenthetic == "N"):
							micro = yninput("Do you like Microsoft? ")
							if (micro == "Y"):
								print("Use F#")
							if (micro == "N"):
								print("Use Haskell")
					
					
				
if (runtime == "N"):
	install = yninput("Are you willing to install something? ")
	while (install!="Y" and install!="N"):
		print("Invalid!")
		install=yninput("> ")
	if (install == "N"):
		os = yninput("Do you use any of the main 3 OSes(Windows, Linux, or MacOS)?")
		while (os!="Y" and os!="N"):
			print("Invalid!")
			os=yninput("> ")
		if (os == "Y"):
			print("Use Bash")
		if (os =="N"):
			print("Use Javascript(or install a more compatible OS)")
	if (install == "Y"):
		spaghetti = yninput("Do you love spaghetti? ")
		if (spaghetti == "Y"):
			future = yninput("Do you care about your future? ")
			if (future == "Y"):
				print("Use PHP")
			if (future == "N"):
				print("Use Perl(and expect to be one day murdered by a future maintainer)")
		if (spaghetti == "N"):
			mods = yninput("do you want to make game mods?")
			if (mods == "Y"):
				print("Use Lua(or java if you play Minecraft)")
			if (mods == "N"):
				indent=("do you like indentations?")
				if (indent == "Y"):
					print("Use Python")
				if (indent == "N"):
					print("Use Ruby")
