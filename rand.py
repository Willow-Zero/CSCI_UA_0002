import random 
random_number = random.randint(1,100)
guess = 0
while guess != random_number:
	guess = int(input("what is your guess? "))
	if guess > random_number:
		print("Too high!")
	elif guess < random_number:
		print("Too low!")
	else:
		print("Congratulations!!")