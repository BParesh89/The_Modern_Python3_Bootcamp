def nth(input_list, index):
	return input_list[index]


# testing
assert(nth(['a', 'b', 'c', 'd'], 1) == 'b')
assert(nth(['a', 'b', 'c', 'd'], -2) == 'c')
assert(nth(['a', 'b', 'c', 'd'], 0) == 'a')
assert(nth(['a', 'b', 'c', 'd'], -4) == 'a')
assert(nth(['a', 'b', 'c', 'd'], -1) == 'd')
assert(nth(['a', 'b', 'c', 'd'], 3) == 'd')
