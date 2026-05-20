tag_one = "shoe, belt, SHOE "
tag_two= " "

def find_top_tag(tag_string):
	
	my_map = dict()
	
	count = 0
	
	most = "NONE"
	
	if tag_string.strip() == "":
		return "NONE"
		
	strings = tag_string.split(",")
	
	for string in strings:
		
		string = string.lower().strip()
			
		if string == "":
			continue
			
		if string in my_map:
			my_map[string] += 1
		else:
			my_map[string] = 1
			
		if my_map[string] > count:
			count = my_map[string]
			most = string
			
	return most
	
print(find_top_tag(tag_one))
print(find_top_tag(tag_two))