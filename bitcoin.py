import sys
import requests


if len(sys.argv) != 2:
	sys.exit("Missing command-line argument")

try:
	amount = float(sys.argv[1])
except ValueError:
	sys.exit("Command-line argument is not a number")

try:
	btc = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=833cadee2d74915e916419da667144b49be142e0721a0f51827f1e48576250ec")
except requests.RequestException:
	sys.exit("API request failed")
	
response = btc.json()
price = float(response["data"]["priceUsd"])
total = price * amount
print(f"${total:,.4f}")
