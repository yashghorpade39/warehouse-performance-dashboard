# -----------------------------
# DHL Project - Maintenance Data Generator
# Table: DIMMAINTENANCE
# -----------------------------

import csv
import random
from faker import Faker
import pandas as pd

# Initialize Faker
fake = Faker('en_US')

# -----------------------------
# User Inputs
# -----------------------------
num_rows = int(input("Enter the number of maintenance records to generate: "))
csv_file = input("Enter the output CSV file name (e.g., dim_maintenance.csv): ")

# -----------------------------
# Optional: Read region names from Excel lookup (for consistency)
# -----------------------------
lookup_file = "/Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/LookupData/LookupFile.xlsx"
region_sheet_name = "State Region Names"

# Read only the unique region names from your existing lookup sheet
df_regions = pd.read_excel(lookup_file, sheet_name=region_sheet_name)
unique_regions = sorted(df_regions['Region'].unique())

# -----------------------------
# Generate Maintenance Data
# -----------------------------
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    header = ['MaintenanceID', 'TechnicianName', 'Team', 'Contact', 'Shift', 'Region']
    writer.writerow(header)

    for i in range(1, num_rows + 1):
        technician_name = fake.name()
        team_name = random.choice([
            'Zone Tech Team',
            'Facility Repairs',
            'Automation Crew',
            'Maintenance Squad',
            'Equipment Ops Team'
        ])
        contact = fake.phone_number()
        shift = random.choice(['Morning', 'Evening', 'Night'])
        region = random.choice(unique_regions)  # <-- uses same regions as warehouse

        row = [i, technician_name, team_name, contact, shift, region]
        writer.writerow(row)

print(f"\n File '{csv_file}' generated successfully with {num_rows} maintenance records.")
