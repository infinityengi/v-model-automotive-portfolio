#!/usr/bin/env python3
import csv
try:
    with open('templates/requirements-template.csv') as f:
        reader = csv.DictReader(f)
        for r in reader:
            print(f"{r['ReqID']}: {r['Title']} -> {r['VerificationMethod']}")
except FileNotFoundError:
    print("No requirements template found.")
