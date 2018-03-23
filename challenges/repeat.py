def repeat(string, num):
    string_list = []
    for i in range(num):
        string_list.append(string)
    return "".join(string_list)


# testing
assert(repeat('pepsi', 3) == 'pepsipepsipepsi')
assert(repeat('*', 2) == '**')
assert(repeat('abc', 0) == '')
