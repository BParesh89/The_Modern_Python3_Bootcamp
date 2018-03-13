def remove_negatives(l):
	return list(filter(lambda num: num >= 0, l))

#testing
assert(remove_negatives([-1,3,4,-99]) == [3,4])
assert(remove_negatives([-7,0,1,2,3]) == [0,1,2,3])
assert(remove_negatives([5,6,7]) == [5,6,7])
