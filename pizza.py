from tabulate import tabulate
import sys
import csv


def main():
	if len(sys.argv) > 2:
		sys.exit("Too many command-line arguments")
	elif len(sys.argv) < 2:
		sys.exit("Too few command-line arguments")
		
	if not sys.argv[1].endswith(".csv"):
		sys.exit("Not a CSV file")
		
	try:
		with open(sys.argv[1]) as f:
			reader = csv.DictReader(f)
			table = list(reader)
	except FileNotFoundError:
		sys.exit("File does not exist")
		
	print(tabulate(table, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
	main()
