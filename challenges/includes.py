def includes(collection, value, index=0):
    if isinstance(collection, list) | isinstance(collection, str):
    	return value in collection[index:]
    else:
        return value in collection.values()


# testing
assert(includes([1, 2, 3], 1) == True)
assert(includes([1, 2, 3], 1, 2) == False)
assert(includes({'a': 1, 'b': 2}, 1) == True)
assert(includes({'a': 1, 'b': 2}, 'a') == False)
assert(includes('abcd', 'b') == True)
assert(includes('abcd', 'e') == False)
