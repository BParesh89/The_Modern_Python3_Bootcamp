from functools import wraps

def ensure_authorized(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs.get('role') == "admin":
			return fn(*args, **kwargs)
		return "Unauthorized"
	return wrapper

#testing
@ensure_authorized
def show_secrets(*args, **kwargs):
	return "Shh! Don't tell anybody!"

assert(print(show_secrets(role="admin")) == "Shh! Don't tell anybody!")
assert(print(show_secrets(role="nobody")) == "Unauthorized")
assert(print(show_secrets('a'="b")) == "Unauthorized")
