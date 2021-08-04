import csv
from statistics import mean
with open("DATA475_lab_rectangles_data.csv", newline="") as f:
    reader = csv.reader(f)
    next(f)


    areas = []
    for row in reader:
        width, length = row[1], row[2]
        area = float(width) * float(length)
        areas.append(area)

summary = {
    "Total count":len(areas),
    "Total Area":sum(areas),
    "Max Area":max(areas),
    "Min Area":min(areas),
    "Avg Area":mean(areas)
    }   

for key in summary: 
    print(f"{key}: {summary[key]}")

with open("summary.csv", mode="w", newline="") as f: 
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values())