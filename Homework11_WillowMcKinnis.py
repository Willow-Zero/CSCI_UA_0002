import turtle as t
def triangle(endnum):
	if endnum > 0:
		return (endnum + triangle(endnum-1))
	else:
		return(0)
print(triangle(int(input("Triangle: "))))
def areWeThereYet(answer):
	if answer == "yes":
		None
	else:
		areWeThereYet(input("Are we there yet? "))
areWeThereYet(input("Are we there yet? "))

def turtle_spiral(length):
	if length == 1:
		t.done()
	else:
		if length % 4 == 0:
			if t.pencolor() == 'black':
				t.pencolor('orange')
			else:
				t.pencolor('black')
		t.forward(length)
		t.left(90)
		turtle_spiral(length-1)
turtle_spiral(int(input("Spiral length: ")))

def swap(twoVals):
#	print("swapping: " + str(twoVals))
	twoVals[0],twoVals[1] = twoVals[1],twoVals[0]
	return(twoVals)

def quicksort(toSort):
#	print(toSort)
	lesser = []
	greater = []
	if len(toSort) <= 1:
		return(toSort)
	if len(toSort) == 2:
		if toSort[0] > toSort[1]:
			return(swap(toSort))
	pivot = toSort[0]
	pivot = [pivot]
	if len(toSort) > 2:
		for num in toSort:
			if num > pivot[0]:
				greater.append(num)
			elif num < pivot[0]:
				lesser.append(num)
#		print("higher: " + str(greater))
#		print("lower: " + str(lesser))
#		print("pivot: " + str(pivot[0]))
	return(quicksort(lesser) + pivot +  quicksort(greater))
print(quicksort([35, 42, 39, 7, 49, 46, 33, 43, 28, 25]))
