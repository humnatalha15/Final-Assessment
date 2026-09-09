import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('regression 4/car data.csv')
print(df.head())
print("df.shape:         " , df.shape)
df.plot.scatter(x='Year', y='Selling_Price', title='Scatter Plot of Year and Selling_Price');
plt.show()
print("df.corr(numeric_only=true):        " , df.corr(numeric_only=True))
print("df.describe():                    " , df.describe())


print(" df['Year'] :     " , df['Year'])
print("  df['Selling_Price']   :    ", df['Selling_Price']   )
y = df['Year'].values.reshape(-1, 1)
X = df['Selling_Price'].values.reshape(-1, 1)
print("y :  " , y)
print("X :   " , X)
print(df['Year'].values) 
print(df['Year'].values.shape)
print(X.shape) 
print(X)
SEED=42
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)
print(X_train) 
print(y_train)      
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
def calc(slope, intercept, Year):
    return slope*Year+intercept

score = calc(regressor.coef_, regressor.intercept_,2014)
print(score)
y_pred = regressor.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')