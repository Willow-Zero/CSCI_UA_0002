import time

def triangle_number():
	num = int(input("What number should I analyze? "))
	add = 0
	while num>0:#uses num as a 'reverse increment' variable, incrementing down every time it adds, then addint the next m, repeat until m is zero.
		add = add+num
		num = num-1
	print(add)

def rect_draw(w,h,c):
	i=0
	while i<h: # while the increment is less than the hight, print the character the number of times given by the width.
		i+=1
		print(c*w)


def parallelo(h,w,c):
	i=0
	while i<h:
		i+=1
		print(" "*(h-i) + c*w) #pretty much the same as the rectangle, just adding h-i spaces at the beginning to shift the shape to a parallelogram.

def printline(h,m,s,f):
	print(h.zfill(2)+":"+m.zfill(2)+":"+s.zfill(2)+"."+f)

def clock():
	hours = 0
	minutes = 0
	seconds = 0
	millis = 0
	while True:
		millis += 1
		if (millis == 10):
			seconds +=1
			millis = 0
		if (seconds == 60):
			minutes +=1
			seconds = 0
		if (minutes == 60):
			hours +=1
			minutes = 0
		if (hours == 24):
			hours = 0
		printline(str(hours),str(minutes),str(seconds),str(millis))
		time.sleep(.1)

choice = ""
while choice != "0":
	choice = input("Which program would you like to run?(1-4, select 0 to quit) " )
	if choice == "1":
		triangle_number()
	if choice == "2":
		width=int(input("Rectangle width: "))
		height=int(input("Rectangle height: "))
		char=input("Rectangle character: ")
		rect_draw(width,height,char)
	if choice == "3":
		width=int(input("Parallelogram width: "))
		height=int(input("Parallelogram height: "))
		char=input("Parallelogram character: ")
		parallelo(height,width,char)
	if choice =="4":
		clock()



		