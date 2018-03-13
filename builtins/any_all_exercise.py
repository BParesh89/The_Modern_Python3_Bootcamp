def is_all_strings(input):
	return all(type(value) == str for value in input)

#testing
assert(is_all_strings(['a','b','c']) == True)
assert(is_all_strings([2,'a','b','c']) == False)
assert(is_all_strings(('hello','goodbye')) == True)
