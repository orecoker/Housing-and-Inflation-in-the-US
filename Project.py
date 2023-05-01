#import necessary libraries
import pandas as pd

#read in files as dataframes
df_h = pd.read_csv('.../Housing Prices 2004-2014 SOURCE.csv')
df_i  = pd.read_csv('.../Inflation 2004-2014 SOURCE.csv')
df_h
df_i

#file path and exported csvs
file_path = '.../FILES/'
h_data = 'Housing Price 2004-2014 CLEAN.csv'
i_data = 'Inflation 2004-2014 CLEAN.csv'

#clean housing dataset and prepare for merging
clean_housing = df_h.loc[(df_h['LOCATION'] == 'USA')]
clean_housing = clean_housing.drop(['INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'Flag Codes'], axis=1)
clean_housing.rename(columns={'Value' : 'Housing Value * 1k'}, inplace=True)
clean_housing
clean_housing.info()

#export clean housing data into csv
clean_housing.to_csv(file_path + h_data, index=False)

#clean inflation dataset and prepare for merging
clean_inflation = df_i.loc[(df_i["LOCATION"] == 'USA')]
clean_inflation = clean_inflation.drop(['INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'Flag Codes'], axis=1)
clean_inflation.rename(columns={'Value' : 'Inflation Value'}, inplace=True)
clean_inflation
clean_inflation.info()

#export clean inflation data into csv
clean_inflation.to_csv(file_path + i_data, index=False)

#merge housing and inflation dataset
merged_hi = clean_housing.merge(clean_inflation, how='inner', on=['TIME', 'LOCATION'])
merged_hi
merged_hi.info()

#analyze data set for average inflation and average housing value and standard deviation for both columns
hmean = merged_hi['Housing Value * 1k'].mean()
print('Average Housing Value between 2004-2014: ', hmean * 1000)

hstd = merged_hi['Housing Value * 1k'].std()
print('Standard Deviation for Housing Value between 2004-2014: ', hstd * 1000)

imean = merged_hi['Inflation Value'].mean()
print('Average Inflation Value between 2004-2014: ', imean)

istd = merged_hi['Inflation Value'].std()
print('Standard Deviation for Inflation Value between 2004-2014: ', istd)

#create scatterplot of relationship between housing price over time
h_scatter = merged_hi.plot.scatter(x='TIME',y='Housing Value * 1k') 

#create scatterplot of relationship between inflation over time
i_scatter = merged_hi.plot.scatter(x='TIME',y='Inflation Value') 

#correlation matrix
results = merged_hi.corr()
matrix = results.unstack()
k = matrix[matrix>0]
l = matrix[matrix<0]

print(k,l)

pd.plotting.scatter_matrix(merged_hi)
