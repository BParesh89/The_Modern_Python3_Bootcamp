# # using map and filter
# def triple_and_filter(l):
# 	return list(map(lambda n: 3*n ,filter(lambda n: n%4 == 0, l)))

# alternatively with list comprehension
def triple_and_filter(l):
	return [3*num for num in l if num % 4 == 0]

# testing
assert(triple_and_filter([1,2,3,4]) == [12])
assert(triple_and_filter([4,8,7,9,12]) == [12,24,36])
