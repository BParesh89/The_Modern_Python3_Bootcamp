def extremes(collection):
	return (min(collection), max(collection))

#testing 
assert(extremes([1,2,3,4,5]) == (1, 5))
assert(extremes((99,25,30,-7)) == (-7, 99))
assert(extremes("alcatraz") == ( 'a', 'z'))
