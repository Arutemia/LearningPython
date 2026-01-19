import random

# Get valid level
while True:
	try:
		level = int(input("Level: "))
		if level > 0:
			break
	except ValueError:
		pass
	
# Generate a random number
random_num = random.randint(1, level)

# Keep guessing
while True:
	try:
		guess = int(input("Guess: "))
		
		if guess < 1:
			continue
			
		if guess < random_num:
			print("Too small!")
		elif guess > random_num:
			print("Too large!")
		else:
			print("Just right!")
			break
	except ValueError:
		pass
		

