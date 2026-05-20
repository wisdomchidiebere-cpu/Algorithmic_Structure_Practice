ai_response = {
    "model_id": "gpt-custom-v2",
    "timestamp": 16845321,
    "data": {
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "The code you provided has a memory leak."
                },
                "confidence_score": 0.98
            },
            {
                "index": 1,
                "message": {
                    "role": "assistant",
                    "content": "Here is the optimized version."
                },
                "confidence_score": 0.45
            }
        ]
    },
    "error": None
}

def extract_best_answer(payload):
	try:
		return payload["data"]["choices"][0]["message"]["content"]
	except (KeyError, IndexError, TypeError):
		return "None"

print(extract_best_answer(ai_response))