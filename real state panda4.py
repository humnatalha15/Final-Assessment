import pandas as pd
sales=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',')
print(sales)
print(sales.dtypes)
print(sales.info())
print(sales.describe())
print(sales.shape)
print(sales.tail(5))
print(sales.head(5))
saleAmount=sales['Sale Amount']
print(saleAmount)
saleAmount_saleRatio=sales[['Sale Amount', 'Sales Ratio']]
print(saleAmount_saleRatio)
salesSingleRow=sales.loc[1]
print(salesSingleRow)
salesSingleRow2=sales.loc[[3,5]]
print(salesSingleRow2)
salesSlice=sales.loc[2:6]
print(salesSlice)
selectionOfRows=sales.loc[sales['Property Type']=='Residential']
print(selectionOfRows)
salesSingleColumn=sales.loc[:1,'Sale Amount']
print(salesSingleColumn)
saleMultipleColumn=sales.loc[:,['Assessed Value', 'Sales Ratio']]
print(saleMultipleColumn)
saleSlice=sales.loc[:1,['Assessed Value','Sales Ratio']]
print(saleSlice)
saleRowColumn=sales.loc[sales['Property Type']=='Residential', 'Assessed Value':'Sales Ratio']
print(saleRowColumn)
sales_index_col=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', index_col='Sale Amount')
print(sales_index_col)
print(sales_index_col.dtypes)
print(sales_index_col.info())
sales1=sales_index_col.loc[248400]
print(sales1)
sales2=sales_index_col.loc[[248400,325000]]
print(sales2)
sales3=sales_index_col.loc[248400 : 239900]
print(sales3)
sales4=sales_index_col.loc[sales_index_col['Property Type']=='Residential']
print(sales4)
sales5=sales_index_col.loc[:248400,'Assessed Value']
print(sales5)
sales6=sales_index_col.loc[:248400,['Assessed Value', 'Sales Ratio']]
print(sales6)
sales7=sales_index_col.loc[:248400,'Address':'Sales Ratio']
print(sales7)
sales8=sales_index_col.loc[sales_index_col['Property Type']=='Residential','Assessed Value':'Sales Ratio']
print(sales8)
sales9=sales_index_col.iloc[3]
print(sales9)
sales10=sales_index_col.iloc[[1,3,5]]
print(sales10)
sales11=sales_index_col.iloc[3:6]
print(sales11)
sales12=sales_index_col.iloc[:,3]
print(sales12)
sales13=sales_index_col.iloc[:,[2,5]]
print(sales13)
sales14=sales_index_col.iloc[:,3:6]
print(sales14)
sales15=sales_index_col.iloc[[1,4,6], 5:6]
print(sales15)
sales.drop(1, axis=0, inplace=True)
sales.drop(index=2, inplace=True)
sales.drop([3, 5], axis=0, inplace=True)
print("Modified DataFrame - Remove Rows:")
print(sales)
sales.drop('Residential Type', axis=1, inplace=True)
sales.drop(columns='Non Use Code', inplace=True)
sales.drop(['Assessor Remarks', 'OPM remarks'], axis=1, inplace=True)
print("Modified DataFrame -  delete Residential Type ,Non USe Code ,Assessor Remarks, OPM remarks,column :")
print(sales)
selected_rows = sales.query("`List Year` == 2020")
print(selected_rows.to_string())
print(len(selected_rows))
sorted_df = sales.sort_values(by='Sales Ratio')
print(sorted_df.to_string(index=False))
df1 = sales.sort_values(by=['Sales Ratio', 'Assessed Value'])
print(df1.to_string(index=False))
grouped = sales.groupby('Sales Ratio')['Assessed Value'].sum()
print(grouped.to_string())
print( len(grouped))
df_cleaned = sales.dropna()
print("Cleaned Data:\n",df_cleaned)
sales.fillna('unknown', inplace=True)
print(sales)