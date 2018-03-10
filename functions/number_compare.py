def number_compare(a,b):
	""" number_compare(a,b) compares a and b, returns which is greater or if equal"""
	if a > b:
		return "First is greater"
	elif a < b:
		return "Second is greater"
	return "Numbers are equal"

# # Testing
# print(number_compare(1,1))
# print(number_compare(1,4))
# print(number_compare(4,1))