total = 0

while total < 50:
	coin = int(input("Insert Coin: "))
	
	if coin in [5, 10, 25]:
		total = coin + total
	
	if total < 50:
		print("Amount Due:", 50 - total)
		
	else:
		print("Change Owed:", total - 50)
		
		
	