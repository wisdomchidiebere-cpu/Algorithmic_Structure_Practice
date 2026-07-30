ages = [25, 50, -10, 20, -18]

valid_ages = [f"{age} years" for age in ages if age > 0]

print(valid_ages)

raw_skills = [" Python ", "java", "PYTHON", " SQL ", "Java"]

unique_skills = { skill.lower().strip() for skill in raw_skills}

print(unique_skills)

tasks = {"fetch_data": 2, "process_image": 15, "save_db": 1, "train_model": 45}

slow_tasks = {task: num for task, num in tasks.items() if num > 10}

print(slow_tasks)