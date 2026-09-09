import pandas as pd
growth=pd.read_csv('startup_growth_investment_data.csv', delimiter=',')
print(growth)
print(growth.dtypes)
print(growth.info())
print(growth.describe())
print(growth.shape)
print(growth.head(5))
print(growth.tail(5))
Industry=growth['Industry']
print(Industry)
Industry_Country=growth[['Industry', 'Country']]
print(Industry_Country)
growthSingleRow=growth.loc[1]
print(growthSingleRow)
growthMultipleRow=growth.loc[[2,3]]
print(growthMultipleRow)
growthSlice=growth.loc[1:5]
print(growthSlice)
selaectionOfRows=growth.loc[growth['Industry']=='Blockchain']
print(selaectionOfRows)
GrowthSingleColumn=growth.loc[:1,'Valuation (USD)']
print(GrowthSingleColumn)
growthmultipleColumn=growth.loc[:,['Industry','Valuation (USD)']]
print(growthmultipleColumn)
growthSliceColumn=growth.loc[:1,'Investment Amount (USD)':'Valuation (USD)']
print(growthSliceColumn)
growthRowColumn=growth.loc[growth['Industry']=='Blockchain', 'Valuation (USD)':'Investment Amount (USD)']
print(growthRowColumn)
growth_index_col=pd.read_csv('startup_growth_investment_data.csv', delimiter=',',index_col='Valuation (USD)')
print(growth_index_col)
print(growth_index_col.dtypes)
print(growth_index_col.info())
growth1=growth_index_col.loc[6621448041.824468]
print(growth1)
growth2=growth_index_col.loc[[6621448041.824468, 8363214103.88975]]
print(growth2)
growth3=growth_index_col.loc[6621448041.824468 :8363214103.88975]
print(growth3)
growth4=growth_index_col.loc[growth_index_col['Industry']=='Blockchain']
print(growth4)
growth5=growth_index_col.loc[:6621448041.824468, 'Industry']
print(growth5)
growth6=growth_index_col.loc[:6621448041.824468, ['Country','Year Founded' ]]
print(growth6)
growth7=growth_index_col.loc[:6621448041.824468,'Country':'Investment Amount (USD)']
print(growth7)
growth8=growth_index_col.loc[growth_index_col['Industry']==' Blockchain','Country':'Investment Amount (USD)']
print(growth8)
growth9=growth_index_col.iloc[3]
print(growth9)
growth10=growth_index_col.iloc[[1,3,5]]
print(growth10)
growth11=growth_index_col.iloc[3:6]
print(growth11)
growth12=growth_index_col.iloc[:,3]
print(growth12)
growth13=growth_index_col.iloc[:,[2,5]]
print(growth13)
growth14=growth_index_col.iloc[:,3:6]
print(growth14)
growth15=growth_index_col.iloc[[1,4,6], 5:6]
print(growth15)
growth.drop(1, axis=0, inplace=True)
growth.drop(index=2, inplace=True)
growth.drop([3, 5], axis=0, inplace=True)
print("Modified DataFrame - Remove Rows:")
print(growth)
growth.drop('Year Founded', axis=1, inplace=True)
growth.drop(columns='Funding Rounds', inplace=True)
growth.drop(['Number of Investors', 'Industry'], axis=1, inplace=True)
print("Modified DataFrame -  delete Year Founded ,Funding Rounds , Number of Investors, Industry,column :")
print(growth)
selected_rows = growth.query("Country == 'Germany'")
print(selected_rows.to_string())
print(len(selected_rows))
sorted_df = growth.sort_values(by='Investment Amount (USD)')
print(sorted_df.to_string(index=False))
df1 = growth.sort_values(by=['Investment Amount (USD)', 'Country'])
print(df1.to_string(index=False))
grouped = growth.groupby('Investment Amount (USD)')['Country'].sum()
print(grouped.to_string())
print( len(grouped))
df_cleaned = growth.dropna()
print("Cleaned Data:\n",df_cleaned)
growth.fillna(0, inplace=True)
print(growth)