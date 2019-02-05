import csv
f = open("Csv.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow("hello")
f.close