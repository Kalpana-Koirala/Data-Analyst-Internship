import openpyxl as pxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Data Dictionary"
headers = (["Variable Name", "Meaning", "Type", "Business Relevance"])
ws.append(headers)

data = [
    ["Order_ID", "Unique identifier assigned to each order", "Categorical (Identifier)",
     "Enables tracking, referencing, and auditing individual orders"],
    ["Order_Date", "Date on which the order was placed", "Date",
     "Supports trend analysis, seasonality detection, and sales forecasting"],
    ["Customer_ID", "Unique identifier assigned to each customer", "Categorical (Identifier)",
     "Enables customer-level analysis such as repeat purchase and loyalty tracking"],
    ["Customer_Name", "Full name of the customer", "Categorical (Text)",
     "Useful for personalization, communication, and CRM records"],
    ["Age", "Age of the customer in years", "Numeric (Discrete)",
     "Helps segment customers by age group for targeted marketing"],
    ["Gender", "Gender of the customer", "Categorical",
     "Supports demographic analysis and gender-based marketing strategies"],
    ["City", "City where the customer is located", "Categorical",
     "Helps identify regional sales patterns and guide location-based strategy"],
    ["Product", "Name of the product purchased", "Categorical",
     "Identifies best-selling and underperforming products"],
    ["Category", "Product category or classification", "Categorical",
     "Enables category-level performance analysis and inventory planning"],
    ["Quantity", "Number of units purchased in the order", "Numeric (Discrete)",
     "Indicates demand volume and helps with inventory and supply planning"],
    ["Unit_Price", "Price per single unit of the product", "Numeric (Continuous)",
     "Used to analyze pricing strategy and profitability"],
    ["Total_Sales", "Total revenue generated from the order (Quantity x Unit_Price)", "Numeric (Continuous)",
     "Key metric for measuring revenue, sales performance, and business growth"],]
for row in data:
    ws.append(row)
wb.save("data_dictionary.xlsx")

import pandas as pd
import numpy as np
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

print(" Missing Values")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include=np.number).columns
df[numeric_columns] = df[numeric_columns].fillna(0)
text_columns = df.select_dtypes(include="object").columns
df[text_columns] = df[text_columns].fillna("N/A")
print(df)

print(" Duplicate Rows ")
print(df.duplicated().sum())
duplicates = df[df.duplicated()]
print(duplicates)

text_columns = df.select_dtypes(include="object").columns
for col in text_columns:
    print(f"\nUnique values in '{col}':")
    print(df[col].unique())
for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.title()
    numeric_columns = df.select_dtypes(include=np.number).columns

df['Order_ID'] = df['Order_ID'].astype(str).str.upper()
df['Customer_ID'] = df['Customer_ID'].astype(str).str.upper()
print(df.columns)

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\nOutliers in '{col}': {len(outliers)} rows")
    print(outliers[[col]])

city_to_region = {
    "Mumbai": "West", "Pune": "West","Delhi": "North","Bengaluru": "South",
    "Hyderabad": "South","Kolkata": "East", "Patna" : "East", "Gaya": "East"}
if 'City' in df.columns:
    df['Region'] = df['City'].map(city_to_region).fillna("Other")
dob_column = df.pop('Region')
df.insert(7, 'Region', dob_column)

from datetime import datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='mixed', dayfirst=True)
df['Date of Birth'] = df.apply(
    lambda row: (row['Order_Date'] - pd.DateOffset(years=int(row['Age']))).date(),axis=1)
df['Order_Date'] = df['Order_Date'].dt.strftime('%d-%m-%Y')
dob_column = df.pop('Date of Birth')
df.insert(4, 'Date of Birth', dob_column)

if {'Quantity', 'Unit_Price'}.issubset(df.columns):
    df['Total_Sales'] = df['Quantity'] * df['Unit_Price']

df.to_excel("cleaned_data.xlsx",index=False)
print("\nCleaned dataset saved as 'ApexPlanet_DataAnalytics_Cleaned.xlsx'")
print(df.shape)
print(df.describe())
print(df.info())
print(df.columns)
print(df.dtypes)
