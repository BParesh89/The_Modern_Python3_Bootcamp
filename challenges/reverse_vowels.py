import re


def reverse_vowels(string):

    # finding the vowels and reversingthem
    pattern = re.compile(r'[aeiou]', re.I)
    result = pattern.findall(string)[::-1]
    result.append('')

    # removing the vowels from the string
    sub = pattern.sub('XXX', string)
    sub_list = sub.split('XXX')

    # joining the reversedvowels and non-vowels
    final = []
    for i in range(0, len(sub_list)):
        final.append(sub_list[i])
        if i - 1 != len(sub_list):
            final.append(result[i])

    return ''.join(final)



# testing
reverse_vowels("Reverse Vowels In A String")
reverse_vowels('aeiou')
assert(reverse_vowels("Hello!") == "Holle!")
assert(reverse_vowels("Tomatoes") == "Temotaos")
assert(reverse_vowels("Reverse Vowels In A String")
       == "RivArsI Vewols en e Streng")
assert(reverse_vowels("aeiou") == "uoiea")
assert(reverse_vowels("why try, shy fly?") == "why try, shy fly?")
