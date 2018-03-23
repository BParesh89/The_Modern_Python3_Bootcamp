def remove_every_other(input_list):
    return [input_list[i] for i in range(len(input_list)) if i % 2 == 0]


# testing
assert(remove_every_other([1, 2, 3, 4, 5]) == [1, 3, 5])
assert(remove_every_other([5, 1, 2, 4, 1]) == [5, 2, 1])
assert(remove_every_other([1]) == [1])
