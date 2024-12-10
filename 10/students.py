import csv

students =[]
with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        student ={"name": row["name"],"roll": row["roll"],"year": row["year"]}
        students.append(student)

for s in sorted(students, key = lambda s: s['roll']):
    print(f"{s['name']} having roll {s['roll']}, {s['year']} year")