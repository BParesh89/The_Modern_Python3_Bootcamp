def min_max_key_in_dictionary(d):
	return [min(d.keys()), max(d.keys())]

# testing
assert(min_max_key_in_dictionary(
    {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}) == [1, 10])
assert(min_max_key_in_dictionary({1: "Elie", 4: "Matt", 2: "Tim"}) == [1, 4])
