def week():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
    	yield day


# testing
days = week()
assert(next(days) == 'Monday')
assert(next(days) == 'Tuesday')
assert(next(days) == 'Wednesday')
assert(next(days) == 'Thursday')
assert(next(days) == 'Friday')
assert(next(days) == 'Saturday')
assert(next(days) == 'Sunday')
