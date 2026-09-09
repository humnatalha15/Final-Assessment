import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv')
print(df.head())
print(df.columns)
print(df.dtypes)
sns.histplot(data=df, x="Assessed Value", bins=30)
plt.title("house prices")
plt.show()
sns.scatterplot(data=df, x="Assessed Value", y="Sale Amount")
plt.title("house prices")
plt.show()
sns.lineplot(data=df, x="Assessed Value", y="Sale Amount")
plt.title("house price")
plt.show
sns.barplot(data=df, x="Assessed Value", y="Sale Amount")
plt.title("house price")
plt.show