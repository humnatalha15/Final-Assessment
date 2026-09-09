import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = 'regression 7/Train.csv'
df = pd.read_csv(path_to_file)

print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)
import seaborn as sns
variables=['Item_Weight','Item_Visibility','Item_MRP']
for var in variables:
    plt.figure()
sns.regplot(x=var, y='Item_Outlet_Sales', data=df).set(title=f'Regression plot of {var} and Item_Outlet_Sales');
plt.show()
read = input("Wait here: \n")


plt.figure()

correlations = df.corr()
print("correlations...\n" , correlations)
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Consumption Data - Pearson Correlations')

plt.show()
read = input("Wait for me....")
y = df['Item_Outlet_Sales']
X = df[['Item_Weight', 'Item_Visibility','Item_MRP']]

SEED = 200
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

print("X.shape # (48, 4):     \n", X.shape )
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("regressor.intercept_......\n", regressor.intercept_)
print("regressor.coef_ " , regressor.coef_)
feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Coefficient value'])
print(coefficients_df)
y_pred = regressor.predict(X_test)


results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)
from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')