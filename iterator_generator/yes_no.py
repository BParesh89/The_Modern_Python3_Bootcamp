def yes_or_no():
	current = 'yes'
	while True:
		yield current
		if current == 'yes':
			current = 'no'
		else: 
			current = 'yes'

# testing
gen = yes_or_no()
assert(next(gen) == 'yes')
assert(next(gen) == 'no')
assert(next(gen) == 'yes')
assert(next(gen) == 'no')
assert(next(gen) == 'yes')