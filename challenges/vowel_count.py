def vowel_count(string):
    return {k: string.lower().count(k) for k in 'aeiou' if string.lower().count(k) > 0}


# testing
assert(vowel_count('awesome') == {'a': 1, 'e': 2, 'o': 1})
assert(vowel_count('bookkeeper') == {'e': 3, 'o': 2})
assert(vowel_count('rhythm') == {})
