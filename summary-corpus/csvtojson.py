import csv
import json

csv_path = "190658G-Corpus .csv"
json_path = "metaphores.json"

data = []
with open(csv_path, encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    data.extend(
        {
            "poem_name": row["Poem Name"],
            "poet": row["Poet"],
            "line": row["Line"],
            "metaphor_present": row["Metaphor present or not"],
            "count":row["count of the metaphor"],
            "metaphorical_terms": row["metaphorical terms"],
            "meaning": row[" Meaning"],
            
        }
        for row in csv_reader
    )
with open(json_path, "w", encoding="utf-8") as f:
    for row in data:
        json.dump({"index": {"_index": "metaphorquest"}}, f)
        f.write("\n")
        json.dump(row, f)
        f.write("\n")
