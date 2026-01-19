import inflect

#create the inflect engine
p = inflect.engine()

#create an empty list for names
names = []

# Keep prompting the user for names
try:
	while True:
		name = input("Name: ")
		
		#add input inside the list names
		names.append(name)
except EOFError:
	print()

# Combine names naturally (adds commas and 'and')
join_names = p.join(names)

# Print the final output
print(f"Adieu, adieu, to {join_names}")
