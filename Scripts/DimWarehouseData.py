# -----------------------------
# DHL Project - Warehouse Data Generator
# Table: DIMWAREHOUSE
# -----------------------------

import pandas as pd
import random
import csv
from faker import Faker

# Initialize Faker for US addresses
fake = Faker('en_US')

# -----------------------------
# User Inputs
# -----------------------------
num_rows = int(input("Enter the number of warehouse records to generate: "))
csv_file = input("Enter the CSV file name (e.g., dim_warehouse.csv): ")

# -----------------------------
# Lookup File Setup
# -----------------------------
lookup_file = "/Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/LookupData/LookupFile.xlsx"

# Sheet: Warehouse Names Data (Adjectives + Nouns)
sheet_warehouse_names = "Warehouse Names Data"
adjective_column = "Adjectives"
noun_column = "Nouns"

# Sheet: State Region Names (State → Region)
sheet_state_region = "State Region Names"
state_column = "State"
region_column = "Region"

# Read both sheets
df_names = pd.read_excel(lookup_file, sheet_name=sheet_warehouse_names)
df_regions = pd.read_excel(lookup_file, sheet_name=sheet_state_region)

# Create a dictionary mapping state → region
state_region_map = dict(zip(df_regions[state_column], df_regions[region_column]))

# -----------------------------
# Data Generation
# -----------------------------
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Define header
    header = [
        'WarehouseID', 'WarehouseName', 'WarehouseType', 'OpenDate',
        'Address', 'City', 'State', 'Country', 'Region', 'ManagerName'
    ]
    writer.writerow(header)

    # Generate each warehouse record
    for i in range(1, num_rows + 1):
        # Generate warehouse name
        adj = df_names[adjective_column].sample(n=1).values[0]
        noun = df_names[noun_column].sample(n=1).values[0]
        warehouse_name = f"{adj} {noun}"

        # Generate address and region
        state = fake.state()
        region = state_region_map.get(state, random.choice(['Northeast', 'Midwest', 'South', 'West']))

        # Create a data row
        row = [
            i,  # WarehouseID
            warehouse_name,
            random.choice(['Distribution Center', 'Sorting Hub', 'Regional Facility', 'Fulfillment Center']),
            fake.date_between(start_date='-10y', end_date='today'),
            fake.address().replace("\n", " ").replace(",", " "),
            fake.city(),
            state,
            "United States",
            region,
            fake.name()
        ]
        writer.writerow(row)

print(f"\n File '{csv_file}' generated successfully with {num_rows} warehouse records.")
