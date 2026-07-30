log_data = " alice-PASS, BOB-fail, charlie-PASS, david-fail, EVE-PASS "

arr = log_data.split(",")

names = [name.strip().lower() for name in arr]

sorted_names = [name.split("-") for name in names if "-pass" in name]

names_with_pass = [name[0] for name in sorted_names]

print(names_with_pass)