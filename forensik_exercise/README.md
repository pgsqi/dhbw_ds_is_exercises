# 🔍 Forensik-Übung: Analyse eines simulierten Datenabflusses

Diese Übung simuliert einen internen Datenabfluss in einer Unternehmensumgebung. Ziel ist es, diesen Vorfall mit Hilfe von Log- und Netzwerkdaten forensisch zu untersuchen.

## 🧠 Ziel der Übung

Du sollst herausfinden:

- Wer hat wann auf welche Daten zugegriffen?
- Welche Daten wurden exfiltriert?
- Welches Verhalten ist auffällig oder „böse“?
- Wie könnte ein solcher Vorfall verhindert werden?

---

## 🧱 Setup (Docker-Umgebung)

### Voraussetzungen

- Docker & Docker Compose installiert
- Python 3 (optional für Datenbank- oder Loggenerator)

### Projektstruktur
forensik_exercise/
├── app/ # Flask-Webanwendung mit Export-Funktion
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── db/ # PostgreSQL-Datenbank mit Beispieldaten
│ └── init.sql
├── attacker/ # Skripte für gutes und böses Verhalten
│ ├── good_user.py
│ └── bad_exporter.py
├── capture/ # Netzwerk-Mitschnitt (pcap-Datei)
├── logs/ # Enthält app.log mit Export-Zugriffen
├── docker-compose.yml
└── README.md # Diese Anleitung



---

## 🚀 Starten der Übung

```bash
docker compose up --build
```

## ⚠️ Bei Bedarf vorher stoppen mit:
```bash
docker compose down
```

## 🌐 Zugriff auf die Webanwendung

Öffne im Browser:
```bash
http://localhost:5050/export?user=alice 
```
## 👥 Simulierte Nutzer

| Nutzer | Verhalten | Beschreibung |
|--------|-----------|--------------|
| `alice` | gut       | manueller Zugriff, 2 Exporte, realistischer Abstand |
| `bob`   | böse      | automatisierter Zugriff, 10 schnelle Requests hintereinander |

---

## 📄 Relevante Dateien

| Datei | Beschreibung |
|-------|--------------|
| `logs/app.log`              | Logfile mit allen Exporten (User + IP + Zeit) |
| `capture/traffic.pcap`      | Netzwerk-Mitschnitt, z. B. zur Analyse mit Wireshark |
| `attacker/bad_exporter.py`  | Skript für "böses" Verhalten |
| `attacker/good_user.py`     | Skript für "gutes" Verhalten |

---

Dies simuliert einen manuellen Export durch eine legitime Nutzerin.

## 🔍 Deine Aufgaben

1. **Starte die Umgebung** mit:

   ```bash
   docker compose up --build
   ```
## 🔍 Analyseaufgaben

### Öffne `logs/app.log` und analysiere:

- Wie oft hat welcher Nutzer exportiert?
- Welche IPs sind beteiligt?
- Gibt es verdächtige Zeitabstände?

### Öffne `capture/traffic.pcap` in Wireshark:

- Gibt es HTTP-POSTs oder verdächtigen Datenverkehr?
- Wurden Daten im Klartext übertragen?
- Welcher Nutzer oder welche IP ist auffällig?

---

## 📘 Bonus (optional)

- Erweitere die App um Benutzer-Login oder Session-IDs
- Füge ein SIEM-System hinzu (z. B. Wazuh, ELK)
- Simuliere verschlüsselten Datenabfluss (z. B. HTTPS)

---

## ✅ Ziel

Am Ende dieser Übung solltest du in der Lage sein:

- Forensische Spuren in Log- und Netzwerkdaten zu erkennen  
- Nutzerverhalten zu unterscheiden  
- Einen forensischen Kurzbericht zu erstellen  

**Viel Erfolg! 🕵️‍♂️**
