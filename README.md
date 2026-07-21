# Data-Analyst-Internship

# Data Immersion & Wrangling
A simple Python script to clean and standardize a sales dataset before analysis. 
It handles missing values, duplicate rows, inconsistent text formatting, mixed date formats, and outlier detection.

# Task Performed
Created a data dictionary,documenting each variable's meaning, type, and potential business relevance.
To identify critical issues: missing values, duplicates,inconsistent formatting, and outliers. 
Missing values: numeric columns filled with 0, text columns filled with "N/A" 
Duplicates: detects and removes duplicate rows 
Inconsistent formatting: standardizes text columns (trims whitespace, title case) Date formatting: parses mixed date formats and converts them all to a single consistent format (dd-mm-yyyy) 
Outlier detection: flags outliers in numeric columns using the IQR (Interquartile Range) method
Feature engineering (e.g., creating new columns like Region from a city column & Date of Birth column from an Age column is an estimate, not the real birth date.
Exports a cleaned Excel file ready for further analysis

# Requirements
Visual Studio Code - Python : Pandas, Numpy, Openpyxl.

# Deliverables:
Output a final, analysis-ready dataset.
