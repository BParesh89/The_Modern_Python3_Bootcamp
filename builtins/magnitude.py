def max_magnitude(l):
	return max(abs(num) for num in l)

# testing
assert(max_magnitude([300,20,-900]) == 900)
assert(max_magnitude([10,11,23]) == 23)