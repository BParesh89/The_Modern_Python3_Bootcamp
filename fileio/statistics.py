def statistics(filename):
	with open(filename) as file:
		text = file.read()

		lines = text.split("\n")
		words = text.split()
		characters = list(text)

	return {"lines":len(lines), "words":len(words), "characters":len(characters)}

print(statistics('story.txt'))