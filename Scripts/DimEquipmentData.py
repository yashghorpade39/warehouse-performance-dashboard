# -----------------------------
# DHL Project - Equipment Data Generator
# Table: DIMEQUIPMENT
# -----------------------------

import pandas as pd
import random
import csv

# -----------------------------
# USER INPUTS
# -----------------------------
num_rows = int(input("Enter the number of equipment records to generate: "))
csv_file = input("Enter the CSV file name (e.g., dim_equipment.csv): ")

# Path to lookup Excel file
excel_file_path_name = "/Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/LookupData/LookupFile.xlsx"
excel_sheet_name_equipment = "Equipment Names"
equipment_column_name = "EquipmentName"

# Read the Equipment Names sheet
df_eq = pd.read_excel(excel_file_path_name, sheet_name=excel_sheet_name_equipment)

# -----------------------------
# EQUIPMENT TYPE MAPPING (Realistic MHE categories)
# -----------------------------
equipment_mapping = {
    "Conveyor Belt": 1,
    "Automated Sorter": 2,
    "Forklift": 3,
    "Pallet Jack": 3,
    "Robotic Arm": 4,
    "Packaging Machine": 5,
    "Barcode Scanner": 6,
    "Weighing Scale": 7,
    "AGV (Automated Guided Vehicle)": 4,
    "Crane": 3,
    "Material Lift": 3,
    "Dock Leveler": 7,
    "Stretch Wrapper": 5,
    "Palletizer": 5,
    "Maintenance Robot": 4
}

# -----------------------------
# MANUFACTURER OPTIONS
# -----------------------------
brands = ['Siemens', 'Honeywell', 'Daifuku', 'Dematic', 'ABB', 'Bosch Rexroth', 'Cognex']

# -----------------------------
# OPEN OUTPUT FILE
# -----------------------------
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Define header
    header = ['EquipmentID', 'EquipmentName', 'EquipmentTypeID', 'Brand', 'PowerRating', 'MaintenanceCycleDays']
    writer.writerow(header)

    # -----------------------------
    # GENERATE ROWS
    # -----------------------------
    for i in range(1, num_rows + 1):
        equipment_name = df_eq[equipment_column_name].sample(n=1).values[0]
        equipment_type_id = equipment_mapping.get(equipment_name, random.randint(1, 7))  # fallback if not in mapping

        row = [
            i,  # EquipmentID
            equipment_name,
            equipment_type_id,  # Foreign key to DIMEQUIPMENTTYPE
            random.choice(brands),
            round(random.uniform(1.5, 10.0), 1),  # PowerRating in kW
            random.choice([15, 30, 45, 60])  # Maintenance cycle in days
        ]

        writer.writerow(row)

print(f"\n File '{csv_file}' generated successfully with {num_rows} equipment records.")
