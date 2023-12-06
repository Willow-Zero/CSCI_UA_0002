import turtle as t



print("First problem")
def switch(list,p1,p2):
	list[p1],list[p2] = list[p2],list[p1]
	return list


def sort(unsort):
	sorted = False
	while sorted == False:
		i = 0
		sorted = True
		for x in range(len(unsort)-1):
			if unsort[i][1] > unsort[i+1][1]:
				switch(unsort,i,i+1)
				sorted = False
			i+=1
	return(unsort)

def scorecalc(Input_Data):
	out = []
	for team in Input_Data:
		score = team[1]+ (team[2]/2)
		print(team[0] + ", " + str(score))
		out.append([team[0],score])
	print(out)
	print(sort(out))

Input_Data = [['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]] 


scorecalc(Input_Data)

print("-----------------------\nSecond Problem")

def CartesianProduct(List1,List2):
	accum = []
	for coord1 in List1:
		for coord2 in List2:
			accum.append([coord1,coord2])
	return(accum)

coord_list_1 = [[-200,200],[-200,90],[-50,-20]]
coord_list_2 = [[50,200],[50,170],[300,90],[50,30],[50,0],[50,-13],[50,-73]]

def draw(coordlist):
	for x in coordlist:
		t.up
		t.setposition(x[0])
		t.down
		t.setposition(x[1])
	t.mainloop()

draw(CartesianProduct(coord_list_1,coord_list_2))


