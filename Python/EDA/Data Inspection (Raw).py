import pandas as pd # for data manipulation and analysis

df = pd.read_csv(r'C:\Users\sulaiman.at\Documents\GitHub\EDA-JB-Property-Transaction\Python\JB Properties Data 2021-2024(TSV).csv', sep='\t')

print('\n\n\n')

df.info()

print('\n\n\n')

print(df.head(5))    # print output of the first n row

print('\n\n\n')

print(df.dtypes)     # print output of the data types by column

print('\n\n\n')

print("\n(Total no. of rows, Total no. of columns) = " + f"{df.shape}")

print('\n\n\n')


