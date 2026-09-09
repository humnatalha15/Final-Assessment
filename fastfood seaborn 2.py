import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df = pd.read_csv('FastFoodRestaurants (1).csv')
print(df.head())
print(df.columns)
print(df.dtypes)
sns.set_theme(style="darkgrid")
sns.lineplot(data=df, x="latitude", y="longitude")
plt.title("fast food restaurant location")
plt.show()
sns.set_theme(style="whitegrid")
sns.scatterplot(data=df, x="longitude", y="latitude")
plt.title('fast food restaurant location')
plt.show()
sns.countplot(data=df, x="province")
plt.title('fast food restaurant')
plt.xticks(rotation=90)
plt.show
sns.boxplot(data=df, x="province", y="latitude")
plt.title('fast food restaurant')
plt.xticks(rotation=90)
plt.show
