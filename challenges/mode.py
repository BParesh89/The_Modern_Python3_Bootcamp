def mode(input_list):
	freq = {k:input_list.count(k) for k in input_list}
	mode = max(freq.values())
	for k,v in freq.items():
		if v == mode:
			return k

#testing
assert(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) == 4)