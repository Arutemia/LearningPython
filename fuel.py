def main():
	fraction = input("Fraction: ")
	try:
		percent = convert(fraction)
		print(gauge(percent))
	except (ValueError, ZeroDivisionError):
		print("Invalid input")

def convert(fraction):
	try:
		X, Y = fraction.split("/")
		X = int(X)
		Y = int(Y)
		if X > Y:
			raise ValueError
		elif Y == 0:
			raise ZeroDivisionError
		else:
			return round((X/Y) * 100)
	except (ValueError, ZeroDivisionError):
		raise
		
def gauge(percentage):
	if percentage <= 1:
		return "E"
	elif percentage >= 99:
		return "F"
	else:
		return f"{percentage}%"


if __name__ == "__main__":
	main()