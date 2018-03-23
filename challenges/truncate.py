def truncate(string, num):
	if num < 3:
		return "Truncation must be at least 3 characters."
	else:
		new_string = string[:num-3]
		if new_string == string:
			return new_string
		else:
			new_string = list(new_string)
			new_string.append('...')
			return ''.join(new_string)





#testing
assert(truncate("Super cool", 2) == "Truncation must be at least 3 characters.")
assert(truncate("Super cool", 1) == "Truncation must be at least 3 characters.")
assert(truncate("Super cool", 0) == "Truncation must be at least 3 characters.")
assert(truncate("Hello World", 6) == "Hel...")
assert(truncate("Problem solving is the best!", 10) == "Problem...")
assert(truncate("Another test", 12) == "Another t...")
assert(truncate("Woah", 4) == "W...")
assert(truncate("Woah", 3) == "...")
assert(truncate("Yo",100) == "Yo")
assert(truncate("Holy guacamole!", 152) == "Holy guacamole!")