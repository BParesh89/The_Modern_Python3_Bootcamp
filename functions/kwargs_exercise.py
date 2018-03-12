def combine_words(word, **kwargs):
	if "prefix" in kwargs:
		return kwargs['prefix'] + word
	elif "suffix" in kwargs:
		return word + kwargs['suffix']
	return word

# testing
assert(combine_words("child") == 'child')
assert(combine_words("child", prefix="man") == 'manchild')
assert(combine_words("child", suffix="ish") == 'childish')
assert(combine_words("work", suffix="er") == 'worker')
assert(combine_words("work", prefix="home") =='homework')