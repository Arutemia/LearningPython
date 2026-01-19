from validator_collection import validators, errors


def main():
	email = input("What's your email address? ")
	
	try:
		validators.email(email)
		print("Valid")
	except errors.InvalidEmailError:
		print("Invalid")

if __name__ == "__main__":
	main()