import json
import csv

# Read JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Convert to CSV
with open("output.csv", "w", newline="") as csv_file:
    # Get headers from JSON keys
    headers = data[0].keys()

    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print("JSON has been converted to CSV successfully.")