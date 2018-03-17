def get_multiples(num=1, count=10):
	for i in range(1,count+1):
		yield num * i
		i += 1

# testing
multiples = get_multiples(3,5)
assert(next(multiples) == 3)
assert(next(multiples) == 6)
assert(next(multiples) == 9)
assert(next(multiples) == 12)
assert(next(multiples) == 15)
