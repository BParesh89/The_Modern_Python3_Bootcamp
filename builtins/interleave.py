def interleave(string1, string2):
	return "".join(["".join(s) for s in list(zip(string1, string2))])

#testing
assert(interleave('hip', 'tim') == "htiipm")
assert(interleave('hto', 'odg') == 'hotdog')
