def multi_letter_count(word):
	return {k:word.lower().count(k) for k in word.lower()}

assert(multi_letter_count("Timmyyyy") == {"t":1, "i":1, "m":2, "y":4})
