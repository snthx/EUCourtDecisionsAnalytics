EU Court Decisions Analytics

# Goal
- Provide robust, statistical analyses of General Court (GC/EuG) and Court of Justice (CJEU/EuGH) decisions to enable empirical statements about case law.

# Concept
- Each decision is mapped to a relevance set: is_relevant (boolean), confidence (percentage), evidence_paragraph_ids (paragraph numbers).
- Input: a topic described as a prompt.
- Output: prepared statistics, including the absolute number of relevant decisions and their evolution over time.
- Data ingestion via the official, machine-readable EUR‑Lex/Publications Office APIs, including CELEX/ECLI identifiers, dates, keywords, and full text; data is stored in a database.
- Relevance classification is AI‑assisted; after classification, key metrics are generated.
- Results are available both as a database table and as prepared summaries; initially exposed via a command-line tool, with a web application planned.

# Advantages over manual research
- Speed: Automates end‑to‑end retrieval and screening.
- Completeness and freshness: Uses official APIs for full, continuously updated coverage.
- Traceability: Every result links back to CELEX/ECLI and source; the process is repeatable and logged.
- Scalability and reuse: Works across topics with the same pipeline, enabling high throughput and consistent methodology.