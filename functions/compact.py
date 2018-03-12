def compact(input_list):
	""" compact(input_list) removes the falsey elements from a list"""
	return [item for item in input_list if item]

# testing
assert(compact([0,1,2,"",[], False, {}, None, "All done"]) == [1,2, "All done"])
