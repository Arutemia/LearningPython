def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")
	

def is_valid(s):
	if not (2 <= len(s) <= 6):
		return False
	
	if not (s[0].isalpha() and s[1].isalpha()):
		return False
	
	if not s.isalnum():
		return False
	
	first_number_found = False
	
	for i in range(len(s)):
		if s[i].isdigit():
			if not first_number_found and s[i] == "0":
				return False
			first_number_found = True
		
		elif first_number_found:
			return False
	
	return True


if __name__ == "__main__":
	main()
