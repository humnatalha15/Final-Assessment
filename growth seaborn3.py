import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df = pd.read_csv('startup_growth_investment_data.csv')
print(df.head())
print(df.columns)
print(df.dtypes)
sns.scatterplot(data=df, x="Investment Amount (USD)", y="Valuation (USD)", hue="Industry")
plt.title("industry growth")
plt.show()
sns.lineplot(data=df, x="Year Founded", y="Growth Rate (%)")
plt.title("industry growth")
plt.show
sns.histplot(data=df, x="Growth Rate (%)", bins=30)
plt.title("industry growth")
plt.show()
sns.countplot(data=df, x="Industry")
plt.title("industry growth")
plt.xticks(rotation=45)
plt.show()
sns.boxplot(data=df, x="Industry", y="Investment Amount (USD)")
plt.title("industry growth")
plt.xticks(rotation=45)
plt.show()
sns.violinplot(data=df, x="Industry", y="Growth Rate (%)")
plt.title("industry growth")
plt.xticks(rotation=45)
plt.show
