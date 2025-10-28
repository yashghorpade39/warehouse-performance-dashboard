# 🏭 DHL MHE Performance Dashboard  

### 📊 End-to-End Data Analytics Project | Snowflake | Power BI | Python  

---

## 🚀 Project Overview  

This project simulates **DHL’s Material Handling Equipment (MHE) performance analysis**, where the goal is to monitor and optimize warehouse operations across multiple locations.  

It covers the **entire data pipeline** — from **data generation using Python**, to **data loading and transformation in Snowflake**, and finally **interactive reporting in Power BI**.  

The dashboard helps answer key operational questions like:  
- Which warehouses are performing best?  
- How does equipment uptime/downtime vary by location?  
- What’s the energy usage and maintenance cost trend over time?  

---

## 🧱 Tech Stack  

| Layer | Tools / Technologies Used |
|-------|---------------------------|
| **Data Generation** | Python, Faker Library |
| **Data Storage** | Snowflake Cloud Data Warehouse |
| **Data Loading** | SnowSQL CLI (PUT & COPY INTO commands) |
| **Visualization** | Power BI Desktop |
| **Documentation & Versioning** | GitHub |

---

## 🔄 Data Pipeline Flow  


### 1️⃣ **Data Generation**
Synthetic data was generated using Python scripts for dimension and fact tables, such as:
- DimWarehouse
- DimEquipmentType
- DimEquipment
- DimMaintenance
- DimDate
- FactPerformance  

Example:  
```python
team_name = random.choice([
    'North Zone Tech Team',
    'Central Maintenance Crew',
    'South Facility Repairs',
    'East Zone Technicians',
    'Warehouse Automation Team'
])

-- Step 1: Upload CSV to Stage
PUT 'file:///Users/yashghorpade/Documents/DHL_MHE_EndToEndProject/OneTimeLoad/DimWarehouse/dim_warehouse.csv'
@TEST_DB.TEST_DB_SCHEMA.TESTSTAGE/dim_warehouse/
AUTO_COMPRESS = FALSE;


-- Step 2: Load from Stage to Table
COPY INTO DimWarehouse (
    WarehouseID,
    WarehouseName,
    WarehouseType,
    OpenDate,
    Address,
    City,
    State,
    Country,
    Region,
    ManagerName
)
FROM @TEST_DB.TEST_DB_SCHEMA.TESTSTAGE/dim_warehouse/dim_warehouse.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');


