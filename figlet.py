from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

# get list of available fonts
fonts = figlet.getFonts()

if len(sys.argv) == 1:
	# if no arguments, random fonts
	chosen_font = random.choice(fonts)

elif len(sys.argv) == 3:
	#if there are three args, accept -f or -font on first array then check if word in
	# array 2 is in fonts variable
	if sys.argv[1] in ["-f" or "--font"] and sys.argv[2] in fonts:
	# assigns the 2nd array to chosen_font variable if both conditions are met
		chosen_font = sys.argv[2]
	else:
		sys.exit("Invalid usage")
else:
	sys.exit("Invalid usage")
	
figlet.setFont(font=chosen_font)

text = input("Input: ")

print(figlet.renderText(text))