def contains_purple(*args):
	return "purple" in args

# testing
assert(contains_purple(25, "purple") == True)
assert(contains_purple("green", False, 37, "blue", "hello world") == False)
assert(contains_purple("purple") == True)
assert(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple") == True)
assert(contains_purple(1,2,3) == False)