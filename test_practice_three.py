#Input:
#groupBy([
 # { name: "Alice", dept: "Engineering" },
  #{ name: "Bob", dept: "Design" },
  #{ name: "Charlie", dept: "Engineering" }
#], "dept")

#//Output:
#{
  #Engineering: [{ name: "Alice", dept: "Engineering" }, { name: "Charlie", dept: "Engineering" }],
  #Design: [{ name: "Bob", dept: "Design" }]
#}



category = [
  { "name": "Alice", "dept": "Engineering" },
  { "name": "Bob", "dept": "Design" },
  { "name": "Charlie", "dept": "Engineering" }
]

def groupBy(arr, arg2):
	my_map = dict()
	
	if len(arr) < 1:
		return my_map
	
	for item in arr:
		if item.get(arg2) in my_map:
			my_map[item.get(arg2)].append(item)
		else:
			my_map[item.get(arg2)] = [item]
			
	return my_map
		
print(groupBy(category, "dept"))

" This code groups objects into a dictionary based on the second arguement. It does this by iterating through an list of objects, then based on the value of the second arguement, it selects the object and creates a key-value pair in the dictionary. The second arguement becomes the key and the all related objects its values. It handles empty arrays by requesting for the first item in the array, if undefined is returned then it signifies that the array is empty, then a string is returned. "