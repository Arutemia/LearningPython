import re


def main():
	print(convert(input("Hours: ")))
	
	
def convert(s):
	pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
	match = re.search(pattern, s)
	if not match:
		raise ValueError
	
	start_h, start_m, start_mer, end_h, end_m, end_mer = match.groups()
	if start_m is None:
		start_m = "00"
	if end_m is None:
		end_m = "00"
		
	start_24 = to_24_hour(start_h, start_m, start_mer)
	end_24 = to_24_hour(end_h, end_m, end_mer)
	
	return f"{start_24} to {end_24}"
	
	
def to_24_hour(hour, minute, meridiem):
	hour = int(hour)
	minute = int(minute)
	if hour < 1 or hour > 12 or minute < 0 or minute > 59:
		raise ValueError
	if meridiem == "AM":
		if hour == 12:
			hour = 0
	else:
		if hour != 12:
			hour += 12
	return f"{hour:02}:{minute:02}"
	

if __name__ == "__main__":
	main()