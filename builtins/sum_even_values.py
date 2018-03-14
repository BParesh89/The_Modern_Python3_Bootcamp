def sum_even_values(*args):
	return sum(num for num in args if num % 2 == 0)

# testing
assert(sum_even_values(1,2,3,4,5,6) == 12)
assert(sum_even_values(1,3,6) == 6)
