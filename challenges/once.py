def once(fn):
	counter=0
	def inner(*args):
		nonlocal counter
		if counter < 1:
			counter+=1
			return fn(*args)
		else:
			return None
	return inner

#testing
def add(a,b):
    return a+b

oneAddition = once(add)

assert(oneAddition(2,2) == 4)
assert(oneAddition(2,2) == None)
assert(oneAddition(12,200) == None)