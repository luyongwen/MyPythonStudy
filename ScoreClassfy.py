#!/usr/bin/env python3
# This is a program for classfy score.
try:
    score = eval(input("Enter your score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    print("Your score class is " + grade, end=".\n")
except:
    print("Input error!")
