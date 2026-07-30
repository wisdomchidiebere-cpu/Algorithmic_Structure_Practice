#flatten_dict({
  #"a": 1,
  #"b": {
    #"c": 2,
    #"d": {
      #"e": 3
   # } }})
#→ {"a": 1, "b.c": 2, "b.d.e": 3}

def flatten_dict(obj, parent_key = "", my_obj = None):
	if my_obj == None:
		my_obj = {}
	
	separator = "."
	
	for key, value in obj.items():
		if parent_key:
			new_key = parent_key + separator + key
		else:
			new_key = key
		if isinstance(value, dict):
			flatten_dict(value, new_key, my_obj)
		else:
			my_obj[new_key] = value
		
	return dict(my_obj)
	

print(flatten_dict({
  "a": 1,
  "b": {
    "c": 2,
    "d": {
      "e": 3
    }
  }
}))
