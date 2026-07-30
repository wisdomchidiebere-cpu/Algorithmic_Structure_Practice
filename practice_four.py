qa_results = [
    {"username": "alice_99", "score": 85},
    {"username": "BOB_builder", "score": 40},
    {"username": "Charlie_Data", "score": 92},
    {"username": "david_script", "score": 55}
]

top_reviewers = [item["username"].lower().strip() for item in qa_results if item["score"] > 80 ]

print(top_reviewers)