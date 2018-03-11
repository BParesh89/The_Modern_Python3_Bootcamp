def single_letter_count(string, letter):
	return len([char for char in string.lower() if char == letter.lower()])

assert(single_letter_count("Hello World!", "l") == 3)
assert(single_letter_count("Hello World!", "h") == 1)
assert(single_letter_count("Hello World!", "x") == 0)