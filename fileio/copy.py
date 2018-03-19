def copy(filename, filename_copy):
	with open(filename_copy, "w") as filecopy:
		with open(filename, 'r') as file:
			file_txt = file.read()

		filecopy.write(file_txt)

copy('story.txt','story_copy.txt')
