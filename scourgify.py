import sys
import csv

def main():
	
	if len(sys.argv) > 3:
		sys.exit("Too many command-line arguments")
	elif len(sys.argv) < 3:
		sys.exit("Too few command-line arguments")
		
	if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
		sys.exit("Not a CSV file")
		
	try:
		with open(sys.argv[1], "r") as input_f:
			reader = csv.DictReader(input_f)
			
			with open(sys.argv[2], "w", newline='') as output_f:
				writer = csv.DictWriter(output_f, fieldnames=["first", "last", "house"])
				writer.writeheader()
				
				for row in reader:
					last, first = row["name"].split(", ")
					writer.writerow({
						"first": first,
						"last": last,
						"house": row["house"]
					})
					
	except FileNotFoundError:
		sys.exit(f"Could not read {sys.argv[1]}")
		

if __name__ == "__main__":
	main()
	
