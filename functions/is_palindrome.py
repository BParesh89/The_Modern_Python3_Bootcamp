# my solution
def is_palindrome(string):
	string = string.lower()
	string = string.replace(" ", "")
	string_list = [char for char in string if char != (" ")]
	reverse = []
	for char in string_list:
		reverse.insert(0,char)
	return string == ''.join(reverse)

#testing
assert(is_palindrome('testing') == False)
assert(is_palindrome('racecar') == True)
assert(is_palindrome('Racecar') == True)
assert(is_palindrome('a man a plan a canal Panama') == True)

# whilst my solution works there was a better solution

# def is_palindrome(string):
#     stripped = string.replace(" ", "")
#     return stripped == stripped[::-1]
