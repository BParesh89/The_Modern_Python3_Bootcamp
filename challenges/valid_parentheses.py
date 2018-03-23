import re

def valid_parentheses(string):
	pattern = re.compile(r'\(+\)+')
	result = pattern.findall(string)
	return ''.join(result) == string


# testing
assert(valid_parentheses("()") == True) 
assert(valid_parentheses(")(()))") == False )
assert(valid_parentheses("(") == False )
assert(valid_parentheses("(())((()())())") == True )
assert(valid_parentheses('))((') == False)
assert(valid_parentheses('())(') == False)
assert(valid_parentheses('()()()()())()(') == False)