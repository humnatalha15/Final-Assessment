import pandas as pd
df=pd.read_csv("RealEstate-USA (1).csv")
print(df)
print(df.columns)
print("df - data types" , df.dtypes)
print("df.info():   " , df.info() )
print('Last three Rows:')
print(df.tail(3))
print('First Three Rows:')
print(df.head(3))
print()
print("Summary of Statistics of DataFrame using describe() method", df.describe())

print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()
state= df['state']
print(state)
print()
state_city= df[['state','city']]
print(state_city)
print()
second_row = df.loc[1]

print(second_row)
second_row2 = df.loc[[1, 3]]

print(second_row2)
second_row3 = df.loc[1:5]

print(second_row3)
second_row4 = df.loc[df['state'] == 'Puerto Rico']
print(second_row4)
second_row5 = df.loc[:1,'state']
print(second_row5)
second_row6 = df.loc[:,['state','city']]
print(second_row6)
second_row7 = df.loc[:1,'price':'state']
print(second_row7)
second_row8 = df.loc[df['state'] == 'Puerto Rico','bed':'city']
print(second_row8)
import pandas as pd
df_index_col=pd.read_csv("RealEstate-USA (1).csv", index_col="brokered_by")
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
second_row = df_index_col.loc[103378]
print(second_row)
second_row2 = df_index_col.loc[[103378, 103379]]
print(second_row2)
second_row3 = df.loc[103378:52707]
print(second_row3)

second_row4 =df_index_col.loc[df_index_col['state'] == 'Puerto Rico']
print(second_row4)


second_row5 = df_index_col.loc[:103379,'state']
print(second_row5)
second_row6 = df_index_col.loc[:103379,['state','city']]
print(second_row6)

second_row7 = df_index_col.loc[:103379,'state']
print(second_row7)
second_row8 = df.loc[df['state'] == 'Puerto Rico','price':'bed']
print(second_row8)
second_row = df.iloc[0]
print(second_row)
second_row2 = df.iloc[[1, 3,5]]
print(second_row2)
second_row3 = df.iloc[2:5]
print(second_row3)
second_row6 = df.iloc[:,[2,4]]
print(second_row6)
second_row7 = df.iloc[:,2:4]
print(second_row7)
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print(second_row8)
df.drop(1, axis=0, inplace=True)
df.drop(index=2, inplace=True)
df.drop([3, 5], axis=0, inplace=True)
print("Modified DataFrame - Remove Rows:")
df.drop('bed', axis=1, inplace=True)
df.drop(columns='status', inplace=True)
df.drop(['street', 'city'], axis=1, inplace=True)
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
print(df)
df.rename(columns= {'state': 'province'}, inplace=True)
df.rename(mapper= {'bed': 'bedroom', 'city':'urban_area'}, axis=1, inplace=True)
print("Modified DataFrame  - Rename Labels :")
print(df)
selected_rows = df.query('province == \'Puerto Rico\' or price > 105000')
print(selected_rows.to_string())
print(len(selected_rows))
sorted_df = df.sort_values(by='price')
print(sorted_df.to_string(index=False))
df1 = df.sort_values(by=['price', 'acre_lot'])

print("Sorting by 'price' (ascending) and then by 'location_id' (ascending):\n")
print(df1.to_string(index=False))
grouped = df.groupby('acre_lot')['price'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))
df_cleaned = df.dropna()
print(df_cleaned)
df.fillna(0, inplace=True)
print(df)
