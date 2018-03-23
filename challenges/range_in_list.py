def range_in_list(input_list, start=0, end=-1):
    if end == -1:
        end = len(input_list)
    return sum(input_list[start:end+1])


# testing
assert(range_in_list([1, 2, 3, 4], 0, 2) == 6)
assert(range_in_list([1, 2, 3, 4], 0, 3) == 10)
assert(range_in_list([1, 2, 3, 4], 1) == 9)
assert(range_in_list([1, 2, 3, 4]) == 10)
assert(range_in_list([1, 2, 3, 4], 0, 100) == 10)
assert(range_in_list([], 0, 1) == 0)
