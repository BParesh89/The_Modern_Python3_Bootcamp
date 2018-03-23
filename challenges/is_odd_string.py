def is_odd_string(string):
	total = sum(ord(char)-96 for char in string)
	return total % 2 == 1

# testing
assert(is_odd_string('a') == True)
assert(is_odd_string('aaaa') == False)
assert(is_odd_string('amazing') == True)
assert(is_odd_string('veryfun') == True)
assert(is_odd_string('veryfunny') == False)
