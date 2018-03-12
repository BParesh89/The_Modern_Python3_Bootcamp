def isEven(num):
	""" isEven(num) returns True or False of a number's evenness"""
	return num % 2 == 0 

def partition(input_list, callback = isEven):
	""" partition(input_list, callback) separates a list into odd and even numbers"""
	truthy_list = []
	falsy_list = []
	for i in input_list:
		if isEven(i):
			truthy_list.append(i)
		else: 
			falsy_list.append(i)
	return [truthy_list, falsy_list]

# testing
assert(partition([1,2,3,4,5], isEven) == [[2,4], [1,3,5]])
