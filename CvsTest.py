#!/usr/bin/env python3
import csv
f = open("Csv.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["hello", "python"])
f.close
