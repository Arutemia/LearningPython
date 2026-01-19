def main():
	tweet = input("Input: ")
	print(shorten(tweet))

def shorten(word):
	output = ""
	for letter in word:
		
		if letter not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
			output = output + letter
	return output


if __name__ == "__main__":
	main()





