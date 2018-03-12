def multiply_even_numbers(input_list):
	result = 1
	for i in input_list:
		if i % 2 == 0:
			result *= i
	if result == 1:
		result = None
	return result

#testing
assert(multiply_even_numbers([2,3,4,5,6]) == 48)
assert(multiply_even_numbers([1,3,5,7]) == None)
