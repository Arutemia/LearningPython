import re


def main():
	print(validate(input("IPv4 Address: ")))


def validate(ip):
	match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
	if not match:
		return False
	
	for group in match.groups():
		if not group.isdigit():
			return False
		if group != str(int(group)):
			return False
		if int(group) < 0 or int(group) > 255:
			return False
		
	return True

if __name__ == "__main__":
	main()
	
