import csv

file_name = "data.csv"

with open(file_name, "r") as file:
    csv_reader = csv.reader(file)
    row_count = sum(1 for row in csv_reader)

print("Total number of rows:", row_count)