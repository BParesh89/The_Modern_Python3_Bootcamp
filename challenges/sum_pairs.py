def sum_pairs(input_list, total):
	for i in range(len(input_list) - 1):
		if input_list[i] + input_list[i+1] == total:
			return [input_list[i], input_list[i+1]]
	return []


#testing 
assert(sum_pairs([4,2,3,6,9], 5) == [2,3])
assert(sum_pairs([18,19,2,10,8],20) == [])
assert(sum_pairs([9,7,3,12,8],20) == [12,8])