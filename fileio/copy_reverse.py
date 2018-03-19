def copy_and_reverse(filename, filename_reversed):
	with open(filename_reversed, "w") as file_reversed:
		with open(filename, "r") as file:
			file_text = file.read()

		reversed_text = file_text[::-1]
		file_reversed.write(reversed_text)

copy_and_reverse('story.txt', 'story_reversed.txt')