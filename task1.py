# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:07:20 2025

@author: JOHN
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset 1_origin.csv')  # Update with your actual filename

# Step 1: Initial Exploration
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# Step 2: Handle Missing Values
df = df.dropna()  # Or use fillna for specific columns

# Step 3: Remove Duplicates
df = df.drop_duplicates()

# Step 4: Standardize Text Fields
text_columns = ['Education', 'Marital_Status']
for col in text_columns:
    df[col] = df[col].str.lower().str.strip()

# Step 5: Fix Date Formats
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

# Step 6: Rename Columns
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Step 7: Convert Data Types
df['income'] = pd.to_numeric(df['income'], errors='coerce')
df['year_birth'] = pd.to_numeric(df['year_birth'], errors='coerce')

# Step 8: Feature Engineering (optional)
df['customer_age'] = 2025 - df['year_birth']
df['total_children'] = df['kidhome'] + df['teenhome']

# Step 9: Save Cleaned Dataset
df.to_csv('cleaned_customer_data.csv', index=False)

# Step 10: Summary
print("Cleaned dataset saved. Final shape:", df.shape)
