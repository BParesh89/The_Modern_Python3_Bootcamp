import re

def is_valid_time(string):
	time_regex = re.compile(r'^(0\d|[1-9]|1\d|[2][0-3]):[0-5]\d$')
	result = time_regex.search(string)
	if result:
		return True
	return False


assert(is_valid_time('12:00') == True)
assert(is_valid_time('00:00') == True)
assert(is_valid_time('11:70') == False)
assert(is_valid_time('91:30') == False)
assert(is_valid_time('12345') == False)
assert(is_valid_time('1:30') == True)
assert(is_valid_time('it is 12:45') == False)
