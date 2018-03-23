def list_check(input_list):
    return all([isinstance(i, list) for i in input_list])


# testing
assert(list_check([[], [1], [2, 3], (1, 2)]) == False)
assert(list_check([1, True, [], [1], [2, 3]]) == False)
assert(list_check([[], [1], [2, 3]]) == True)
