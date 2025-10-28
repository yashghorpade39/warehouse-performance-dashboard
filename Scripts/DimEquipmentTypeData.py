import pandas as pd
import random

# Define Equipment Types that match IDs used in DIMEQUIPMENT mapping
equipment_types = [
    "Conveyor Systems",       # ID = 1
    "Automated Sorters",      # ID = 2
    "Lifting Equipment",      # ID = 3 (e.g., Forklift, Crane, Pallet Jack)
    "Robotics",               # ID = 4 (e.g., Robotic Arm, AGV, Maintenance Robot)
    "Packaging Machines",     # ID = 5 (e.g., Palletizer, Wrapper)
    "Scanning Devices",       # ID = 6 (e.g., Barcode Scanner)
    "Weighing Systems"        # ID = 7 (e.g., Dock Leveler, Weighing Scale)
]

automation_levels = ['Manual', 'Semi-Automated', 'Fully Automated']

# Generate data rows
rows = []
for i in range(1, len(equipment_types) + 1):
    rows.append({
        'EquipmentTypeID': i,
        'TypeName': equipment_types[i - 1],
        'MaxCapacity': random.randint(1000, 5000),
        'AutomationLevel': random.choice(automation_levels)
    })

# Create DataFrame
df = pd.DataFrame(rows)

# Save to CSV
df.to_csv('dim_equipmenttype.csv', index=False)

print(df)
print("\n File 'dim_equipmenttype.csv' generated successfully.")
