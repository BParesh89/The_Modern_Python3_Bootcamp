def sum_floats(*args):
	return sum(arg for arg in args if type(arg) == float)

#testing
assert(sum_floats(1,2.5,3,4.1, "hahah why is there a string here", [], 1.0) == 7.6)
assert(sum_floats(1,2,3,4,5) == 0)