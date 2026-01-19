import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE)
if matches:
	print(f"Username:", matches.group(1))