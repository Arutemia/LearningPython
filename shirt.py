import sys
import os
from PIL import Image, ImageOps


def main():
	if len(sys.argv) > 3:
		sys.exit("Too many command-line arguments")
	elif len(sys.argv) < 3:
		sys.exit("Too few command-line arguments")
		
	valid_ext = (".jpg", ".jpeg", ".png")
	input_ext = os.path.splitext(sys.argv[1])[1].lower()
	output_ext = os.path.splitext(sys.argv[2])[1].lower()
	
	if input_ext != output_ext:
		sys.exit("Input and output extension must be equal")
	
	if input_ext not in valid_ext or output_ext not in valid_ext:
		sys.exit("Invalid extension")
		
	if not os.path.exists(sys.argv[1]):
		sys.exit("File does not exist")
		
	try:
		with Image.open("shirt.png") as shirt:
			with Image.open(sys.argv[1]) as muppet:
				muppet_resized = ImageOps.fit(muppet, shirt.size)
				muppet_resized.paste(shirt, (0, 0), shirt)
				muppet_resized.save(sys.argv[2])
				
	except FileNotFoundError:
		sys.exit("File not found")
		
		
if __name__ == "__main__":
	main()
	
