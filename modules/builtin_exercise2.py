def contains_keyword(*args):
	import keyword
	return any(keyword.iskeyword(s) for s in args)

#testing
assert(contains_keyword("hello", "goodbye") == False)
assert(contains_keyword("def", "haha", "vegemite") == True)
assert(contains_keyword("four", "for", "fore") == True)