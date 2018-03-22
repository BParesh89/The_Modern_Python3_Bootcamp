import re

def censor(string):
	swear_pattern = re.compile(r'\bfrack[a-z]*\b', re.I)
	return swear_pattern.sub('CENSORED', string)

assert(censor('Frack you') == 'CENSORED you')
assert(censor('You Fracking fracker') == 'You CENSORED CENSORED')
assert(censor('I hope you fracking die') == 'I hope you CENSORED die')