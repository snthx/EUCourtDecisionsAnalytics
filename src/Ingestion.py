# Ablauf: Scraping von Entscheidungen des EuGH/EuG


# Kennungen für EuGH-Entscheidungen:
#
# Aktenzeichen / Case number (z. B. C‑123/18)
# Das vom Gericht vergebene, menschenlesbare Aktenzeichen. Wichtig für Suche/Referenz, aber nicht immer eindeutig ohne Gerichtskontext (Court of Justice vs General Court). 
# 
# CELEX‑Nummer (z. B. 62018CJ0123)
# EUR‑Lex interne, stabile ID für EU‑Rechtsakte und Urteile.
# Für EuGH‑Urteile übliche Form: 6 + Jahr(4-stellig) + CJ (Court of Justice) + Verfahrensnummer (4-stellig, führende Nullen).
# Gut für automatischen Abruf über EUR‑Lex (uri=CELEX:...).
# Vollständige CELEX-Liste lässt sich dem IUROPA-Projekt entnehmen
#
# ECLI (European Case Law Identifier, z. B. ECLI:EU:C:2018:123)
# Europäischer Standardidentifier für Entscheidungen. Aufbau: ECLI:EU:C:<Jahr>:<Nummer>. ECLI ist zweckmäßig für Interoperabilität über Datenbanken hinweg. Achtung: Die letzte Ziffer(n) ist eine laufende Nummer der Entscheidungen und nicht dieselbe wie das Aktenzeichen; oft muss sie aus einer Quelle (EUR‑Lex/Curia) übernommen werden — nicht direkt aus C‑Nummern herleitbar.
#
# Curia‑Interne IDs / Curia‑URL (z. B. die Fall‑ID/Parameter in der curia.europa.eu‑URL)
# Die Seiten von curia.europa.eu haben interne Identifikatoren/URLs, die man beim Scrapen verwenden kann. Gut für direkter Zugriff auf die Gerichtsseite, aber datenbank‑spezifisch.

# Example case: EuGH, Urt. v. 21.12.2023 – C-333/21 (European Superleague ESL)
# CELEX: Document 62021CJ0333
# ECLI: ECLI:EU:C:2023:1035
# https://curia.europa.eu/juris/document/document.jsf?text=&docid=280765&pageIndex=0&doclang=en&mode=lst&dir=&occ=first&part=1&cid=24072543

import requests
import os
import csv

# Gets judgments from EUR-Lex by CELEX number
# Input: CELEX number (e.g. 62018CJ0123)
# Output: HTML file with judgment text
def get_judgment_by_celex(celex):
    url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}"
    headers = {"User-Agent": "python-requests/eur-lex-download-script"}
    
    zielverzeichnis = "../data/judgements/"
    os.makedirs(zielverzeichnis, exist_ok=True)
        
    output = os.path.join(zielverzeichnis, f"{celex}.html")

    r = requests.get(url, headers=headers, timeout=30)
    if r.status_code == 200 and "html" in r.headers.get("Content-Type", ""):
        with open(output, "w", encoding="utf-8") as f:
            f.write(r.text)
        # print(f"Saved to {output}")
        log_download_status(celex, True)
    else:
        log_download_status(celex, False)
        # raise RuntimeError(f"Fehler beim Herunterladen: HTTP {r.status_code}")

# Documents whether a judgement is successfully retrieved
# Input: CELEX number, success status (True/False)
# Output: Appends a log entry to download_log.csv
def log_download_status(celex, status):
    from datetime import datetime

    log_file = "../data/download_log.csv"
    
    # Erstellen Sie das Verzeichnis, falls es nicht existiert
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Überprüfen, ob die Datei existiert, um die Header zu schreiben
    file_exists = os.path.isfile(log_file)
    
    with open(log_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["CELEX", "Status", "Timestamp"])  # Header schreiben
        writer.writerow([celex, status, datetime.now().isoformat()])  # Daten schreiben

# Resets the data folder and CSV log file
# Input: Folder path, CSV file path
# Output: Empties the folder and resets the CSV file with header
def reset_folder_and_csv(folder_path, csv_file_path):
    # Leeren des Ordners
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Datei löschen
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)  # Verzeichnis löschen (nur leer)
            except Exception as e:
                print(f"Fehler beim Löschen von {file_path}: {e}")
    
    # Zurücksetzen der CSV-Datei
    header = ["CELEX", "downloaded", "timestamp"]  # Header definieren
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)  # Header schreiben


if __name__ == "__main__":
    reset_folder_and_csv("../data/judgements/", "../data/download_log.csv")
    get_judgment_by_celex("62021CJ0333") # Example CELEX for testing
    get_judgment_by_celex("asdf")  # Invalid CELEX to test error handling
    get_judgment_by_celex("62021CJ0333") # Duplicate to test logging