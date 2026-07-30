#group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#→ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(arr):
	if len(arr) < 1:
		return []
	
	my_map = dict()
		
	for item in arr:
		key = "".join(sorted(item.lower()))
		
		if key in my_map:
			my_map[key].append(item)
		else:
			my_map[key] = [item]
			
	return list(my_map.values())
		
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

#This is a code that groups anagrams together. The code loops through a list of words and utilizing the concept that anagrams have the same letters, it rearranges each word to be able to group them together into a dictionary, when all words are grouped it then appends the grouped words into a list which is then returned. It also handles edge cases by returning an empty list early.