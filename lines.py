import sys

def main():
	if len(sys.argv) > 2:
		sys.exit("Too many command-line arguments")
	elif len(sys.argv) < 2:
		sys.exit("Too few command-line arguments")
		
	if not sys.argv[1].endswith(".py"):
		sys.exit("Not a Python file")
		
	try:
		with open(sys.argv[1]) as f:
			lines = f.readlines()
	except FileNotFoundError:
		sys.exit("File does not exist")
	
	count = 0
	for line in lines:
		line_strip = line.lstrip()
		if line_strip == "" or line_strip.startswith("#"):
			continue
		count += 1
		
	print(count)
	
if __name__ == "__main__":
	main()
		