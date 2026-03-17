# Simple Cybersecurity Log Analyzer

with open("server_logs.txt", "r") as file:
    logs = file.readlines()

for line in logs:
    if "Failed login" in line:
        print("WARNING: Failed login attempt ->", line.strip())

    if "192.168.1.100" in line:
        print("ALERT: Suspicious IP detected ->", line.strip())
