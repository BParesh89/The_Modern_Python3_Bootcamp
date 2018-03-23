def two_list_dictionary(l1, l2):
    if len(l2) > len(l1):
        return dict(zip(l1, l2))
    else:
        for i in range(0, len(l1)-len(l2)):
            l2.append(None)
        return dict(zip(l1, l2))


# testing
assert(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) == {
       'a': 1, 'b': 2, 'c': 3, 'd': None})
assert(two_list_dictionary(['a', 'b', 'c'], [
       1, 2, 3, 4]) == {'a': 1, 'b': 2, 'c': 3})
assert(two_list_dictionary(['x', 'y', 'z'], [1, 2])
       == {'x': 1, 'y': 2, 'z': None})
