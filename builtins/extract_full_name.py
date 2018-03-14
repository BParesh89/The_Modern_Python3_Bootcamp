def extract_full_name(names_dict):
	return [f'{name["first"]} {name["last"]}' for name in names_dict]

# testing
names = [{'first': 'Tim', 'last': 'Thatcher'}, {'first': 'Desi', 'last': 'Cochrane'}]
assert(extract_full_name(names) == ['Tim Thatcher', "Desi Cochrane"])
