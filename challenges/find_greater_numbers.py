def find_greater_numbers(input_list):
    total = 0
    for i in range(len(input_list)):
        for j in input_list[i:]:
            if input_list[i] < j:
                total += 1
    return total


# testing
assert(find_greater_numbers([1, 2, 3]) == 3)
assert(find_greater_numbers([6, 1, 2, 7]) == 4)
assert(find_greater_numbers([5, 4, 3, 2, 1]) == 0)
assert(find_greater_numbers([]) == 0)
