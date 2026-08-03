import requests
import json

ORCID = "0000-0002-5716-4941"

url = f"https://pub.orcid.org/v3.0/{ORCID}/works"

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

publications = []

for work in data["group"]:
    summary = work["work-summary"][0]

    title = summary["title"]["title"]["value"]

    year = ""
    if summary.get("publication-date"):
        year = summary["publication-date"].get("year", {}).get("value", "")

    doi = ""

    for external_id in summary.get("external-ids", {}).get("external-id", []):
        if external_id.get("external-id-type") == "doi":
            doi = external_id.get("external-id-value")

    publications.append({
        "title": title,
        "year": year,
        "doi": doi
    })


with open("data/publications.json", "w") as f:
    json.dump(publications, f, indent=2)

print(f"Saved {len(publications)} publications")
