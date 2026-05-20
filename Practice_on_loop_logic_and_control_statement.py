login_logs = [
    {"user": "alice", "status": "success", "threat_level": 1},
    {"user": "admin", "status": "failed", "threat_level": 5},
    {"user": "bob", "status": "success", "threat_level": 2},
    {"user": "charlie", "status": "failed", "threat_level": 9},
    {"user": "david", "status": "success", "threat_level": 1}
]

for items in login_logs:
	if items["threat_level"] > 8:
		break
	if items["user"] == "admin":
		continue
	if items["status"] == "success" and items["threat_level"] < 3:
		print("Access Granted: " + items["user"])