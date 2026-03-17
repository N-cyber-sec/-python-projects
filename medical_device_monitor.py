# Medical Device Network Monitor

suspicious_ips = [
    "192.168.1.150",
    "192.168.1.200"
]

device_logs = [
    "HeartMonitor connected from 192.168.1.10",
    "InfusionPump connected from 192.168.1.150",
    "MRI scanner connected from 192.168.1.45",
    "Ventilator connected from 192.168.1.200"
]

for log in device_logs:
    for ip in suspicious_ips:
        if ip in log:
            print("ALERT: Suspicious medical device activity ->", log)