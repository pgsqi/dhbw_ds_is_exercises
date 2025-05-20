from flask import Flask, send_file, request
import psycopg2
import csv
import logging

logging.basicConfig(filename='/tmp/app.log', level=logging.INFO)


app = Flask(__name__)

@app.route('/export')
def export_data():
    from flask import request
    user = request.args.get('user', 'unknown')
    client_ip = request.remote_addr

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="db"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()

        filepath = f"/tmp/export_{user}.csv"
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'email', 'iban'])
            writer.writerows(rows)

        cur.close()
        conn.close()

        logging.info("EXPORT by user=%s from IP=%s", user, client_ip)
        return send_file(filepath, as_attachment=True)

    except Exception as e:
        logging.error("EXPORT FAILED by user=%s: %s", user, e)
        return "Internal Server Error", 500
