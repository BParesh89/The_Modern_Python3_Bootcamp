def three_odd_numbers(input_list):
    return any([sum(input_list[i:i+3]) % 2 == 1 for i in range(0, len(input_list)-2)])

# testing
assert(three_odd_numbers([1, 2, 3, 4, 5]) == True)
assert(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]) == True)
assert(three_odd_numbers([5, 2, 1]) == False)
assert(three_odd_numbers([1, 2, 3, 3, 2]) == False)
