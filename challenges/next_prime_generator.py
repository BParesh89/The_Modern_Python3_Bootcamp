def next_prime():
    num = 2
    while True:
        if len([i for i in range(1, num+1) if (num/i) == num//i]) != 2:
            num += 1
        else:
            yield num
            num += 1


# testing
primes = next_prime()
assert([next(primes) for i in range(25)] == [2, 3, 5, 7, 11, 13, 17, 19,
                                             23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
