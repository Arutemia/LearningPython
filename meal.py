def main():
	time_str = input("What time is it? ")
	time_float = convert(time_str)
	
	if 7.0 <= time_float <= 8.0:
		print("breakfast time")
	elif 12.0 <= time_float <= 13.0:
		print("lunch time")
	elif 18.0 <= time_float <= 19.0:
		print("dinner time")

def convert(time):
	hours, minutes = time.split(":")
	time_converted = int(hours) + int(minutes) / 60
	return time_converted

if __name__ == "__main__":
  	main()