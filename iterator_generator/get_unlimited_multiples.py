def get_unlimited_mulitples(num=1):
    current = num
    while True:
        yield current
        current += num


# testing
sixes = get_unlimited_mulitples(6)
sixes_list = [next(sixes) for i in range(15)]
assert(sixes_list == [6, 12, 18, 24, 30, 36,
                      42, 48, 54, 60, 66, 72, 78, 84, 90])
