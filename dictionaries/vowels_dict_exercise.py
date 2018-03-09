# make a dict such that answer = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# use a dict method or dict comprehension

# dict method
answer = {}.fromkeys(['a','e','i','o','u'],0)
print(answer)

# dict comprehension
answer = {k:0 for k in 'aeiou'}
print(answer)