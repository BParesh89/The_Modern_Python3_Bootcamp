def find_the_duplicate(input_list):
	for char in input_list:
		if input_list.count(char) > 1:
			return char
	return None



#testing
assert(find_the_duplicate([1,2,1,4,3,12]) == 1)
assert(find_the_duplicate([6,1,9,5,3,4,9]) == 9)
assert(find_the_duplicate([2,1,3,4]) == None)