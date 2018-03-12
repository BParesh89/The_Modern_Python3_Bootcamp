def frequency(input_list, search):
	return input_list.count(search)

#testing
assert(frequency([1,2,3,4,4,4], 4) == 3)
assert(frequency([True, False, True, True], False) == 1)