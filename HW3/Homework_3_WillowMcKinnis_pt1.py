

def fun1():
	num = int(input('Which number should I analyze? '))
	if (num%2==0):
		print("even")
	else:
		print("odd")
	if (num%3==0):
		print("divisible by 3")
	if (num==0):
		print("zero")


def fun2():
	num = int(input("What number should I analyze: "))
	if (num%2==0 and num%3!=0):
		return(True)
	if (num%2!=0 and num%3==0):
		return(True)
	else:
		return(False)

def generate_truth_table():
	print("|---------------------------------------------------------------|")
	print("|   p\t|   q\t|  p==q\t|  p!=q\t|  p&q\t|p or q\t|  !p\t|  !q\t|")
	combos(True,True)
	combos(True,False)
	combos(False,True)
	combos(False,False)
	print("|---------------------------------------------------------------|")

def combos(p,q):
	print("| "+str(p)+"\t| "+str(q)+"\t| "+str(p==q)+"\t| "+str(p!=q)+"\t| "+str(p and q)+"\t| "+str(p or q)+"\t| "+str(not p)+"\t| "+str(not q)+"\t|")

choice = input("Which problem would you like to run? 1, 2, or 3? seleect 4 to quit.")
while (choice != "4"):
	while (choice != "1" and choice!="2" and choice!="3"):
		choice = input("Invalid. Please enter 1, 2, or 3. ")
	if (choice == "1"):
		fun1()
	if (choice == "2"):
		print(fun2())
	if (choice == "3"):
		generate_truth_tables()
	choice = input("Which problem would you like to run? 1, 2, or 3? seleect 4 to quit. ")