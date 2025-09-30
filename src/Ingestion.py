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
        print(f"Saved to {output}")
    else:
        raise RuntimeError(f"Fehler beim Herunterladen: HTTP {r.status_code}")
    
if __name__ == "__main__":
    get_judgment_by_celex("62021CJ0333")