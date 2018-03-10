# write a function that returns the last element of a list, returns none if empty list

def last_element(input_list):
	""" last_element(input_list) returns the last element of input_list. Default return None"""
	if input_list:
		return input_list[-1]
	return None
