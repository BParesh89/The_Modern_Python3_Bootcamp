import re

def parse_date(string):
	date_regex = re.compile(r'^(?P<d>0[1-9]|[12]\d|3[01])[\.,/](?P<m>0\d|1[0-2])[\.,/](?P<y>\d{4})$')
	result = date_regex.search(string)
	if result:
		return {'d': result.group('d'), 'm': result.group('m'), 'y': result.group('y')}
	return None


assert(parse_date('01/05/2004') == {'d': '01', 'm': '05', 'y': '2004'})
assert(parse_date('27.12.2094') == {'d': '27', 'm': '12', 'y': '2094'})
assert(parse_date('29,02,2012') == {'d': '29', 'm': '02', 'y': '2012'})
assert(parse_date('01/53/2000') == None)
assert(parse_date('91/03/2000') == None)
assert(parse_date('05/07/20004838') == None)
