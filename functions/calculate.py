def calculate(**kwargs):
	lookup_dict = {
		'add': kwargs.get('first', 0) + kwargs.get('second',0),
		'subtract': kwargs.get('first', 0) - kwargs.get('second',0),
		'multiply': kwargs.get('first', 0) * kwargs.get('second',0),
		'divide': kwargs.get('first', 0) / kwargs.get('second',0)
	}
	if kwargs.get('make_float'):
		value = float(lookup_dict[kwargs.get('operation')])
	else: 
		value = int(lookup_dict[kwargs.get('operation')])

	final = f"{kwargs.get('message', 'The result is')} {value}"

	return final

# # I WAS SUPPOSED TO DO IT USING **kwargs, this was my first attempt, will redo above using **kwargs
# def calculate(make_float, operation, first, second, *args, message = "The result is", **kwargs):
# 		if operation == 'add':
# 			if make_float:
# 				return f"{message} {float(first + second)}"
# 			return f"{message} {int(first + second)}"
# 		elif operation == 'subtract':
# 			if make_float:
# 				return f"{message} {float(first - second)}"
# 			return f"{message} {int(first - second)}"
# 		elif operation == 'multiply':
# 			if make_float:
# 				return f"{message} {float(first * second)}"
# 			return f"{message} {int(first * second)}"
# 		else:
# 			if make_float:
# 				return f"{message} {float(first / second)}"
# 			return f"{message} {int(first * second)}"

# testing
assert(calculate(make_float=False, operation='add', message='You just added', first=2, second=4) == "You just added 6")
assert(calculate(make_float=True, operation='divide', first=3.5, second=5) == "The result is 0.7")
assert(calculate(make_float=True, operation='multiply', message='You just multiplied', first=2, second=7) == "You just multiplied 14.0")
assert(calculate(make_float=True, operation='subtract', first=50, second=5) == "The result is 45.0")

