# Aufteilung in White-, Grey- und Blacklist
# Input: Strukturierte Daten (JSON, CSV, SQLite)
# Output: Kategorisierte Daten (White-, Grey-, Blacklist)
# Schritte:
# 1. Einlesen der strukturierten Daten
# 2. Anwendung von Regeln/Kriterien zur Kategorisierung
#       a) White-List: Eindeutig relevante Entscheidungen => Qualifizierung mittels Schlagworten, bspw. Art. 101, 102 AEUV
#       b) Grey-List: Entscheidungen mit unklarer Relevanz => KI-gestützte Entscheidung
#       c) Black-List: Eindeutig irrelevante Entscheidungen
# 3. Speicherung der kategorisierten Daten in separaten Dateien/Tabellen

