type = input()
# will place triple dots between words after splitting the input words,
# this prevents .join to put triple dots between characters
type = "...".join(type.split())
print(type)
