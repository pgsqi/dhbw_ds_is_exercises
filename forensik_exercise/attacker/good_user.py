import time
import requests

# Simuliere normalen manuellen Nutzer: 2 Exporte mit Abstand
users = ["alice"]

for user in users:
    print(f"Requesting export for {user}...")
    r = requests.get(f"http://webapp:5000/export?user={user}")
    print(f"Status: {r.status_code}")
    time.sleep(10)  # wartet 10 Sekunden zwischen Zugriffen
