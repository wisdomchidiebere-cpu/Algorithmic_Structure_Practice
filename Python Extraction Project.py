import re


messy_log = """
[2026-05-12 08:14] TXN_ID: 8091 | STATUS: SUCCESS | AMT: $450.00
[2026-05-12 08:15] TXN_ID: 8092 | STATUS: FAILED | AMT: $NaN | ERR: TIMEOUT
[2026-05-12 08:16] TXN_ID: 8093 | STATUS: SUCCESS | AMT: $12.50
[2026-05-12 08:17] TXN_ID: 8094 | STATUS: PENDING | AMT: $0.00
"""

def extract_revenue(log_data):
      pattern = r"\$\d+(?:\.\d+)?"
      lines = log_data.split("\n")
      revenue = 0
      for line in lines:
            if "SUCCESS" in line:
                 price = re.findall(pattern, line)
                 for number in price:        
      	            number = number.replace("$", " ").strip()
      	            revenue += float(number)
      return "$" + str(revenue)
      
print(extract_revenue(messy_log))

def count_status(log_data):
	lines = log_data.split("\n")
	pattern = r"STATUS:\s([A-Z]+)"
	my_dict = dict()
	for line in lines:
			status = re.findall(pattern, line)
			for word in status:
				if word in my_dict:
				   my_dict[word] += 1
				else:
					 my_dict[word] = 1
					 
	return my_dict
	
print(count_status(messy_log))