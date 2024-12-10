import csv,sys

name = sys.argv[1]
roll = sys.argv[2]

with open("college.csv","a",newline='') as file:
    writer = csv.writer(file)

    writer.writerow([name,roll])