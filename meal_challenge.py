def main():
	time_str = input("What time is it? ").lower().strip()
	time_float = convert(time_str)
	
	if 7.0 <= time_float <= 8.0:
		print("breakfast time")
	elif 12.0 <= time_float <= 13.0:
		print("lunch time")
	elif 18.0 <= time_float <= 19.0:
		print("dinner time")

def convert(time):
	is_am = "am" in time
	is_pm = "pm" in time
	
	time = time.replace("am", "").replace("pm", "").strip()
	
	hours_str, minutes_str = time.split(":")
	hours = int(hours_str)
	minutes = int(minutes_str)
	
	
	if is_pm and hours != 12:
		hours = hours + 12
	elif is_am and hours == 12:
		hours = 0
	
	return hours + minutes / 60
	

if __name__ == "__main__":
  	main()