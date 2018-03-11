def list_manipulation(input_list, command, location, value = 0):
	if command == "remove":
		if location == "end":
			return input_list.pop()
		return input_list.pop(0)
	else:
		if location == "end":
			input_list.append(value)
			return input_list
		input_list.insert(0,value)
		return input_list

# tests
assert(list_manipulation([1,2,3], "remove", "end") == 3)
assert(list_manipulation([1,2,3], "remove", "beginning") == 1)
assert(list_manipulation([1,2,3], "add", "beginning", 17) == [17, 1, 2, 3])
assert(list_manipulation([1,2,3], "add", "end", 17) == [1, 2, 3, 17])