import time
import requests

for i in range(10):
    r = requests.get("http://webapp:5000/export?user=bob")
    print(f"[{i}] Status: {r.status_code}")
    time.sleep(1)
