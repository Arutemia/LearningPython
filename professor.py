import random

def main():
	level = get_level()
	score = 0
	
	for i in range(10):
		x = generate_integer(level)
		y = generate_integer(level)
		
		for _ in range(3):
			try:
				answer = input(f"{x} + {y} = ")
				if int(answer) == (x + y):
					score = score + 1
					break
				else:
					print("EEE")
			except ValueError:
				print("EEE")
				continue
				
		else:
			print(f"{x} + {y} = {x + y}")
	print(f"Score: {score}")
	
	
def get_level():
	while True:
		try:
			level = int(input("Level: "))
			if level > 0 and level <= 3:
				return level
		except ValueError:
			continue

def generate_integer(level):
	if level == 1:
		return random.randint(0,9)
	elif level == 2:
		return random.randint(10,99)
	elif level == 3:
		return random.randint(100, 999)
		

if __name__ == "__main__":
    main()