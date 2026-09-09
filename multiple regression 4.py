import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = 'regression 6/StudentsPerformance.csv'
df = pd.read_csv(path_to_file)

print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)


import seaborn as sns 
variables = ['math score', 'reading score', 'writing score']

for var in variables:
    plt.figure()
    sns.regplot(x=var, y='reading score', data=df).set(title=f'Regression plot of {var} and reading score');
    plt.show()

read = input("Wait here: \n")
plt.figure()
correlations = df.corr(numeric_only=True)
print("correlations...\n" , correlations)
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Consumption Data - Pearson Correlations')

plt.show()
read = input("Wait for me....")
y = df['reading score']
X = df[['math score',
       'writing score', 'reading score']]
SEED=200
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

#After splitting the data, we can train our multiple regression model. Notice that now there is no need to reshape our X data, once it already has more than one dimension:
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
actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)