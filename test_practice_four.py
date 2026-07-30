#flatten([1, [2, 3], [4, [5, 6]]], 1)
#→ [1, 2, 3, 4, [5, 6]]

#flatten([1, [2, [3, [4]]]], 2)
#→ [1, 2, 3, [4]]

num_list = [1, [2, 3], [4, [5, 6]]]
example = []

def flatten(arg1, arg2 = 1):
	new_list = []
	
	if not arg1:
		return new_list
	
	for item in arg1:
		if isinstance(item, list):
			new_list.extend(item)
		else:
			new_list.append(item)

	if (arg2 > 1):
		return flatten(new_list, arg2 - 1)

	return new_list

print(flatten(num_list))

#This is a code that flattens a nested list based on a depth provided which is the second arguement(arg2). It implements the use of recursion to flatten the list to the required depth. It also handles an empty list by returning new_list early if the length is found to be less than one.