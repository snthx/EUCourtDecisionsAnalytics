# Aufteilung in White-, Grey- und Blacklist
# Input: html-Datei mit Volltext der Entscheidung auf Englisch
# Output: Kategorisierte Daten (White-, Grey-, Blacklist)
# Schritte:
# 1. Einlesen der strukturierten Daten
# 2. Anwendung von Regeln/Kriterien zur Kategorisierung
#       a) White-List: Eindeutig relevante Entscheidungen => Qualifizierung mittels Schlagworten, bspw. Art. 101, 102 AEUV
#       b) Grey-List: Entscheidungen mit unklarer Relevanz => KI-gestützte Entscheidung
#       c) Black-List: Eindeutig irrelevante Entscheidungen
# 3. Speicherung der kategorisierten Daten in separaten Dateien/Tabellen

import os
import csv
from datetime import datetime

def is_relevant(judgement):
    """
    Überprüft, ob das Urteil relevant ist.
    Gibt True zurück, wenn es in der White- oder Grey-List ist, sonst False.
    """

    # Wenn whitelist_check(judgement) True zurückgibt, wird greylist_check(judgement) nicht aufgerufen,
    # da der or-Operator eine Kurzschlussauswertung verwendet.
    return whitelist_check(judgement) or greylist_check(judgement)

def whitelist_check(judgement):
    # Implementiere die Kriterien für die White-List
    keywords = ["101", "Art. 102 AEUV"]
    return any(keyword in judgement for keyword in keywords)

def greylist_check(judgement):
    # Dummy-Implementierung für die Grey-List
    # Hier KI-Einsatz
    return False

def classify_judgements():
    judgement_dir = "../data/judgements/"
    results = []

    # Schritt 1: Einlesen der HTML-Dateien im Verzeichnis
    for filename in os.listdir(judgement_dir):
        if filename.endswith(".html"):
            file_path = os.path.join(judgement_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                judgement_content = f.read()
                # Schritt 2: Kategorisierung
                print(f"Classifying {filename}...")
                relevant = is_relevant(judgement_content)
                celex = filename[:-5]  # Entfernen des Suffixes ".html"
                timestamp = datetime.now().isoformat()
                results.append((celex, relevant, timestamp))

    # Schritt 3: Speicherung der kategorisierten Daten in einer CSV-Datei
    save_classified_data("classified_judgements.csv", results)

def save_classified_data(csv_file, data):
    """
    Speichert die klassifizierten Daten in einer CSV-Datei.
    """
    csv_file = "../data/classification_log.csv"
    
    # Erstellen Sie das Verzeichnis, falls es nicht existiert
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    
    # Überprüfen, ob die Datei existiert, um die Header zu schreiben
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["CELEX", "is_relevant", "timestamp"])  # Header schreiben
        for celex, is_relevant, timestamp in data:
            writer.writerow([celex, is_relevant, timestamp])  # Daten schreiben

def reset_csv(csv_file_path):
    # Zurücksetzen der CSV-Datei
    header = ["CELEX", "is_relevant", "timestamp"]  # Header definieren
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)  # Header schreiben

if __name__ == "__main__":
    reset_csv("../data/classification_log.csv")
    classify_judgements()