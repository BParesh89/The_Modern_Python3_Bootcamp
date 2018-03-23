def running_average():
	total = 0
	counter = 0
	def inner(num):
		nonlocal total, counter
		total += num
		counter += 1
		return round(total/counter,2)
	return inner



#testing
rAvg = running_average();
assert(rAvg(10) == 10.0)
assert(rAvg(11) == 10.5)
assert(rAvg(12) == 11)

rAvg2 = running_average()
assert(rAvg2(1) == 1)
assert(rAvg2(3) == 2)