from functools import wraps


def only_ints(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if not all([type(arg) == int for arg in args]):
			return "Please only invoke with integers"
		return fn(*args, **kwargs)
	return wrapper

@only_ints
def add(x,y):
	return x+y

assert(add(1,3)==4)
assert(add('1','3') == "Please only invoke with integers")
