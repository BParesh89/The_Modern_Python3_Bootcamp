def titleize(string):
	string_list = string.split(' ')
	str_list = []
	for word in string_list:
		word = word[0].upper() + word[1:]
		str_list.append(word)
	return ' '.join(str_list)


# testing

assert(titleize('this is awesome') == 'This Is Awesome')
assert(titleize('thIs is. aweSOMe') == 'ThIs Is. AweSOMe')