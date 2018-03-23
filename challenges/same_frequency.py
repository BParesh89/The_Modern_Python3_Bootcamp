def same_frequency(num1, num2):
	d1 = {k:list(str(num1)).count(k) for k in list(str(num1))}
	d2 = {k:list(str(num2)).count(k) for k in list(str(num2))}
	return d1 == d2

# testing
assert(same_frequency(551122,221515) == True)
assert(same_frequency(321142,3212215) == False)
assert(same_frequency(1212, 2211) == True)