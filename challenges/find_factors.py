def find_factors(num):
	return [x for x in range(1,num+1) if (num/x) == num//x]


# testing
assert(find_factors(10) == [1, 2, 5, 10])
assert(find_factors(11) == [1, 11])
assert(find_factors(111) == [1, 3, 37, 111])
assert(find_factors(321421) == [1, 293, 1097, 321421])
assert(find_factors(412146) == [1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126, 3271,
                                6542, 9813, 19626, 22897, 29439, 45794, 58878, 68691, 137382, 206073, 412146])
