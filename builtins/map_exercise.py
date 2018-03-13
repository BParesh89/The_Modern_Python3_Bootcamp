def decrement_list(l):
	return list(map(lambda num: num - 1, l))

#testing
assert(decrement_list([1,2,3]) == [0,1,2])
assert(decrement_list([10,20,30]) == [9,19,29])
