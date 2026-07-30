llm_output = " Symptom: HEADACHE | Conf: 0.92, Symptom: nausea | Conf: 0.85, Symptom:  headache  | Conf: 0.92, Symptom: COUGH | Conf: 0.40, Symptom: Fever | Conf: 0.88 "

arr = llm_output.split(",")

names = {item.split("|")[0].split(":")[1].lower().strip() for item in arr if float(item.split("|")[1].split(":")[1]) > 0.80}

sorted_names = sorted(names)

print(" - ".join(sorted_names))