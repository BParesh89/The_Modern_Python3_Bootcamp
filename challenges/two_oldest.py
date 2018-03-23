def two_oldest_ages(input_list):
    while len(input_list) > 2:
        input_list.remove(min(input_list))
    input_list.sort()
    return input_list


# testing
assert(two_oldest_ages([1, 2, 10, 8]) == [8, 10])
assert(two_oldest_ages([6, 1, 9, 10, 4]) == [9, 10])
assert(two_oldest_ages([4, 25, 3, 20, 19, 5]) == [20, 25])
