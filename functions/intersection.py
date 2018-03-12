def intersection(list1, list2):
	return list(set(list1) & set(list2))

# testing
assert(intersection([1,2,3], [2,3,4]) == [2,3])
assert(intersection(['a','b','z'], ['x','y','z']) == ['z'])
