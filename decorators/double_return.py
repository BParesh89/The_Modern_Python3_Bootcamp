from functools import wraps

def double_return(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		return [fn(*args, **kwargs) for i in [1,2]]
	return wrapper

#testing
@double_return
def add(x,y):
	return x+y

assert(add(3,4) == [7,7])