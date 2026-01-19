def meow(n: int) -> str:
	"""Meow n times.
	
	
	:param n: Number of time to meow
	:type n: int
	:raise TypeError: If n not an int
	:return: A string of meows, one per line
	:rtype: str
	"""
	return "meow\n" * n
		
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")