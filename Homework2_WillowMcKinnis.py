import math
# exercise 1
def ex1():
	# set variables
	Day_of_week = input("What is the day of the week? ")
	Month = input("What is the month? ")
	Day_of_month = input("What is the day of the month? ")
	Year = input("What is the year? ")
	# print date
	print(f'{Day_of_week}, {Month} {Day_of_month}, {Year}')

#exercise 2
def ex2():
	print("""The newscaster said, "And Now for Something Completely Different!"\n\nOne quote: ', Two quotes “, Red Quotes, Blue Quotes""")

#exercise 3
def ex3():
	print('5' + '4') #this line adds the two numbers not as INT but as STR, so it prints '54', concatenating the numbers rather than adding them
	print(5 + 4)     #because this line had the numbers has INT literals, when added they are treated as numbers.
#exercise 4
def ex4():
	output = int('5') + int('4') #converts string literals to ints, so they can be added together
	print(output)

def ex5():
	output = (((5*5)/5)-5) # Order of Ops is parenthesis, exponents, multiplication/division, addition/subtraction
	print(output)
	output = (5-((5**5)*5))
	print(output)
	output = ((60-(40*1.5)+(5**2))-25)
	print(output)
def ex6():
	remaining_amount = int(input("What is the cost in pennies? "))
	quarters = remaining_amount // 25 #divide getting the integer, then get the remainder and set remaining_amount equal to that. repeat for nickels.
	remaining_amount = remaining_amount % 25
	nickels = remaining_amount // 5
	remaining_amount = remaining_amount % 5
	pennies = remaining_amount
	print(quarters,'quarters',nickels,'nickels',pennies,'pennies')

def function_1(a,b,c): # this is a seperate function because a later exercise uses the same functionality. it simply returns the 3-number average.
	avg = (a + b + c)/3
	return(avg)

def ex7():
	in1 = int(input("First number: "))
	in2 = int(input("Second number: "))
	in3 = int(input("Third number: "))
	print(function_1(int1,int2,int3)) # takes input and averages

def ex8():
	Input = input('> ')
	print("You entered:")# takes input and then repeats
	print(Input)
	print(Input,Input,Input)

def ex9():
	in1 = int(input("First number: "))
	in2 = int(input("Second number: "))
	in3 = int(input("Third number: "))
	in4 = int(input("Fourth number: "))
	in5 = int(input("Fifth number: "))
	in6 = int(input("Sixth number: ")) # see exercise 7
	print(function_1(in1,in2,in3) + function_1(in4,in5,in6))
	
def ex10(): # i didnt round these biorhythms, unlike in the example. I figure accuracy is valuable in pseudoscience.
	days = int(input('How many days old are you? '))
	prhythm = math.sin((2*(math.pi)*days)/23)
	erhythm = math.sin((2*(math.pi)*days)/28)
	irhythm = math.sin((2*(math.pi)*days)/33)
	print(f'Physical: {prhythm} Emotional: {erhythm} Intellectual {irhythm}')

exercise = input('Which exercise would you like to execute (1-10)? ')
if exercise == "1":
	ex1()
elif exercise == "2":
	ex2()
elif exercise == "3":
	ex3()
elif exercise == "4":
	ex4()
elif exercise == "5":
	ex5()
elif exercise == "6":
	ex6()
elif exercise == "7":
	ex7()
elif exercise == "8":
	ex8()
elif exercise == "9":
	ex9()
elif exercise == "10":
	ex10()


