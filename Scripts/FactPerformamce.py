# -----------------------------
# DHL Project - Fact Performance Data Generator (auto-detect version)
# -----------------------------

import pandas as pd
import numpy as np
import random

# -----------------------------
# USER INPUTS
# -----------------------------
num_rows = int(input("Enter the number of performance records to generate: "))
csv_file = input("Enter the CSV file name (e.g., fact_performance.csv): ")

# -----------------------------
# LOAD DIMENSION TABLES (auto detect counts)
# -----------------------------
dim_warehouse = pd.read_csv('/Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/dim_warehouse.csv')
dim_equipment = pd.read_csv('/Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/dim_equipment.csv')
dim_maintenance = pd.read_csv('/Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/dim_maintenance.csv')

# Automatically get record counts
num_warehouses = len(dim_warehouse)
num_equipment = len(dim_equipment)
num_maintenance_teams = len(dim_maintenance)

print(f" Warehouses: {num_warehouses}, Equipment: {num_equipment}, Maintenance Teams: {num_maintenance_teams}")

# -----------------------------
# GENERATE BASE FACT DATA
# -----------------------------
date_start = np.datetime64('2015-01-01')
date_end = np.datetime64('2025-09-30')

data = {
    'RecordID': range(1, num_rows + 1),
    'DateID': np.random.choice(np.arange(date_start, date_end), size=num_rows),
    'WarehouseID': np.random.randint(1, num_warehouses + 1, size=num_rows),
    'EquipmentID': np.random.randint(1, num_equipment + 1, size=num_rows),
    'MaintenanceID': np.random.randint(1, num_maintenance_teams + 1, size=num_rows)
}

df = pd.DataFrame(data)
df['DateID'] = pd.to_datetime(df['DateID']).dt.strftime('%Y%m%d').astype(int)

# -----------------------------
# ADD PERFORMANCE METRICS
# -----------------------------
df['UptimeHours'] = np.round(np.random.uniform(16, 24, size=num_rows), 2)
df['DowntimeHours'] = np.round(24 - df['UptimeHours'], 2)
df['PackagesProcessed'] = (df['UptimeHours'] * np.random.randint(150, 400, size=num_rows)).astype(int)
df['EnergyUsed_kWH'] = np.round(df['UptimeHours'] * np.random.uniform(3.0, 6.0, size=num_rows), 2)
df['ThroughputRate'] = np.round(df['PackagesProcessed'] / df['UptimeHours'], 2)
df['MaintenanceCost'] = np.round(df['DowntimeHours'] * np.random.uniform(50, 200), 2)

# -----------------------------
# EXPORT TO CSV
# -----------------------------
df.to_csv(csv_file, index=False)

print(f"\n File '{csv_file}' generated successfully with {num_rows} records.")
# print(f" Example preview:\n")
# print(df.head(10))
