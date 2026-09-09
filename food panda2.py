import pandas as pd
food=pd.read_csv("FastFoodRestaurants (1).csv", delimiter=',')
print(food)
print(food.dtypes)
print(food.info())
print(food.tail(4))
print(food.head(4))
print(food.describe())
print(food.shape)
country=food['country']
print(country)
country_city=food[['country', 'city']]
print(country_city)
food1=food.loc[[4,5]]
print(food1)
food2=food.loc[2:4]
print(food2)
food3=food.loc[food["city"]=='Englewood']
print(food3)
food4=food.loc[:1,'city']
print(food4)
food5=food.loc[:,['country', 'keys']]
print(food5)
food6=food.loc[:1,'country':'city']
print(food6)
food7=food.loc[food['city']=='Englewood', 'country':'keys']
print(food7)
food_index_col=pd.read_csv("FastFoodRestaurants (1).csv",delimiter=',', index_col='longitude')
print(food_index_col)
print(food_index_col.dtypes)
print(food_index_col.info())
food8=food_index_col.loc[-74.89021]
print(food8)
food9=food_index_col.loc[[-74.89021, -83.44526]]
print(food9)
food10=food_index_col.loc[-74.89021:-74.84553]
print(food10)
food11=food_index_col.loc[food_index_col["city"]=='Englewood']
print(food11)
food12=food_index_col.loc[:-74.89021,"city"]
print(food12)
food13=food_index_col.loc[:-74.89021,["city","country"]]
print(food13)
food14=food_index_col.loc[:-74.89021,'province':'websites']
print(food14)
food15=food_index_col.loc[food_index_col["city"]=='Athens','province':'websites']
print(food15)
food16=food_index_col.iloc[1]
print(food16)
food17=food_index_col.iloc[[1,3,5]]
print(food17)
food18=food_index_col.iloc[2:5]
print(food18)
food19=food_index_col.iloc[:,3]
print(food19)
food20=food_index_col.iloc[:,[3,5]]
print(food20)
food21=food_index_col.iloc[:,2:6]
print(food21)
food22=food_index_col.iloc[[1,4,6], 4:6]
print(food22)
food.drop(1, axis=0, inplace=True)
food.drop(index=2, inplace=True)
food.drop([3, 5], axis=0, inplace=True)
print("Modified DataFrame - Remove Rows:")
print(food)
food.drop('websites', axis=1, inplace=True)
food.drop(columns='province', inplace=True)
food.drop(['postalCode', 'keys'], axis=1, inplace=True)
print("Modified DataFrame -  websites ,province , postalCode, keys, column :")
print(food)
foodQuery = food.query('city == \'Hamilton\' or latitude >449213 ')
print(foodQuery.to_string())
print(len(foodQuery))
foodSorted = food.sort_values(by='latitude')
print(foodSorted.to_string(index=False))
foodSorted1= food.sort_values(by=['city', 'longitude'])
print(foodSorted1.to_string(index=False))
grouped = food.groupby('city')['latitude'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))

df_cleaned = food.dropna()
print(df_cleaned)
food.fillna(0, inplace=True)
print( food)
