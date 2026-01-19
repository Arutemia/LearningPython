camel_case = input("camelCase: ")
snake = "snake_case: "

for letter in camel_case:
	if letter.isupper():
		snake = snake + "_" + letter.lower()
	else:
		snake = snake + letter.lower()

print(snake, end="")

