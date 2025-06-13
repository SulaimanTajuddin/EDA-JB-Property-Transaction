import pandas as pd # for data manipulation and analysis
import numpy as np
import matplotlib.pyplot as plt # for plotting graph
import seaborn as sns

df = pd.read_csv(r'C:\Users\sulaiman.at\Documents\GitHub\EDA-JB-Property-Transaction\Python\JB Properties Data 2021-2024(TSV).csv', sep='\t')

print(df.head(),'\n\n\n')   # print output of the first n row

print(df.dtypes,'\n\n\n')     # print output of the data types by column

print("\n(Total no. of rows, Total no. of columns) = " + f"{df.shape}\n\n\n") 

print("\nExisting column :\n " + f"{df.columns.tolist()}\n") # inspect column name, view any whitespace

df.columns = df.columns.str.strip() # strip column that has whitespace

print("\nColumn after stripped :\n" + f"{df.columns.tolist()}\n") # output after column stripped

df = df.dropna(axis=1, how='all') # remove the entire column only if all values are NaN

print("\nResult after remove NaN column :\n"+ f"{df.columns.tolist()}\n") # output after stripped NaN column

for i in df.columns:
    print(i," : ",df[i].isnull().sum()) # checking total null values in a column

print(df.duplicated().sum(),'\n\n\n')

# Clean and convert 'Transaction Price' to numeric 
df['Transaction Price'] = df['Transaction Price'].str.replace('RM', '', regex=False)
df['Transaction Price'] = df['Transaction Price'].str.replace(',', '', regex=False).astype(float)

print(df['Land/Parcel Area'].unique())
print(df['Land/Parcel Area'][df['Land/Parcel Area'] == ''])  # find empty strings

# Clean and convert 'Land/Parcel Area' to numeric 
df['Land/Parcel Area'] = df['Land/Parcel Area'].str.replace(',', '', regex=False).astype(float)

print(df['Main Floor Area'].unique())
print(df['Main Floor Area'][df['Main Floor Area'] == ''])  # find empty strings

# Clean and convert 'Main Floor Area' to numeric 
df['Main Floor Area'] = df['Main Floor Area'].str.replace('-', '', regex=False)
df['Main Floor Area'] = df['Main Floor Area'].str.replace(',', '', regex=False).replace('', np.nan).astype(float)

# Extract transaction year (2021-2024))
df['Transaction Year'] = df['Month, Year of Transaction Date'].str.extract(r'(\d{4})').astype(int)

# Scatterplot Transaction Price vs Main Floor Area
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(df['Main Floor Area'],df['Transaction Price'])
ax.set_xlabel('(Main Floor Area)')
ax.set_ylabel('(Transaction Price)')
plt.show()

# Boxplot for detecting outliers
df.select_dtypes(include='number').boxplot(figsize=(20, 8), rot=45, grid=False)
plt.title("Boxplots of Numeric Features")
plt.tight_layout()
plt.show()

# Histogram
df.hist(bins=15, figsize=(10, 6), color='red', edgecolor='black')
plt.suptitle('Histograms of Columns', fontsize=16)
plt.subplots_adjust(hspace=0.5)  
plt.show()

# KDE plot
plt.figure(figsize=(12,	4))
sns.kdeplot(df['Transaction Price'], fill=True,	color='blue', alpha=0.6)
plt.title(f'Kernel Density Estimate(KDE) - Sale Price',	fontsize=16)
plt.xlabel('Sale Price', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Heatmap - checking correlation between the features
plt.figure(figsize=(35,	20))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
plt.show()

# Distribution of transaction price
plt.figure(figsize=(14, 6))
sns.histplot(df['Transaction Price'], bins=50, kde=True, color='red') 
plt.title('Distribution of Sale Price')
plt.xlabel('Transaction Price')
plt.ylabel('count')
plt.show()
print(f"\nSkewness of Transaction Price: {df['Transaction Price'].skew():.2f}")
print(f"Kurtosis of Transaction Price: {df['Transaction Price'].kurt():.2f}")

sns.regplot(x='Land/Parcel Area', y='Transaction Price', data=df, line_kws={"color": "red"})
plt.title("Regression Line: Transaction Price vs. Land/Parcel Area")
plt.xlabel("Land/Parcel Area")
plt.ylabel("Transaction Price")
plt.tight_layout()
plt.show()


