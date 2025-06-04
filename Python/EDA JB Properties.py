import pandas as pd # for data manipulation and analysis
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\sulaiman.at\Documents\GitHub\EDA-JB-Property-Transaction\Python\JB Properties Data 2021-2024(TSV).csv', sep='\t')
#---------------------------------------------------------------------------------------------------------------------
'''
# Overview of raw data + Data inspection:

print(df.head(5))                      # print output of the first n row
print(df.dtypes)                       # print output of the data types by column
print("\n(Total no. of rows, Total no. of columns) = " + f"{df.shape}")
print("\nNull values (True/False):\n") 
print(df.isnull())                     # Check for null values in all cell, returns print output True/False for each cell
print("\nTotal sum of duplicated values = " + f"{df.duplicated().sum()}\n")

'''
#---------------------------------------------------------------------------------------------------------------------
# Data cleansing and filtering starts here:

# Step 1: Clean column names
df.columns = df.columns.str.strip() # The strip() method removes any leading and trailing whitespace from a string.

# Step 2: Extract transaction year (filtering)
df['Transaction Year'] = df['Month, Year of Transaction Date'].str.extract(r'(\d{4})').astype(int)

# Step 3:Clean and convert 'Transaction Price' to numeric 
df['Transaction Price'] = df['Transaction Price'].str.replace('RM', '', regex=False)
df['Transaction Price'] = df['Transaction Price'].str.replace(',', '', regex=False).astype(float)

# Step 4: Filter data for the years 2021 to 2024
filtered_df = df[df['Transaction Year'].isin([2021, 2022, 2023, 2024])]

#----------------------------------------------------------------------------------------------------------------------
# Analysis starts here:

# Step 1: Calculate median and standard deviation by year
summary_by_year = filtered_df.groupby('Transaction Year')['Transaction Price'].agg(
    Median ='median',Std_Dev='std',Mean='mean',Min='min',Max='max'
    ).reset_index()

# Step 2: Display result
print(summary_by_year)






