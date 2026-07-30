#twoSum([2, 7, 11, 15], 9) → [0, 1]
#twoSum([3, 4, 6], 10) → [1, 2]

def two_sum(arr, num):
	if not arr:
		return []
		
	my_map = dict()
		
	for i in range(len(arr)):
		complement = num - arr[i]
			
		if complement in my_map:
			return [my_map[complement], i]
		
		my_map[arr[i]] = i
		
	return []

print(two_sum([2,7,11,15], 9))


#The code returns the indices of the sum of a target number. It does this by looping through the list, grouping the numbers and their indices into a dictionary, getting the complement of the targeted number and checking if it's in the dictionary, if found it returns a sorted list of the required indices. It also handles edge cases by returning an empty list.