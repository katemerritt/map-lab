import os
import json
from scholarly import scholarly

scholar_id = os.environ["SCHOLAR_ID"]

author = scholarly.search_author_id(scholar_id)
author = scholarly.fill(author)

publications = []

for pub in author["publications"]:
    details = pub["bib"]

    publications.append({
        "title": details.get("title", ""),
        "authors": details.get("author", ""),
        "year": details.get("pub_year", ""),
        "journal": details.get("venue", ""),
        "url": pub.get("pub_url", ""),
        "citations": pub.get("num_citations", 0)
    })

with open("data/publications.json", "w") as f:
    json.dump(publications, f, indent=2)

print(f"Saved {len(publications)} publications")
