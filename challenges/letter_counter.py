def letter_counter(string):
    def inner(char):
        return string.lower().count(char)
    return inner


# testing
counter = letter_counter('Amazing')
assert(counter('a') == 2)
assert(counter('m') == 1)

counter2 = letter_counter('This Is Really Fun!')
assert(counter2('i') == 2)
assert(counter2('t') == 1)
