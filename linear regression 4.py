import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('regression 6/StudentsPerformance.csv')
print(df.head())
print("df.shape:         " , df.shape)
df.plot.scatter(x='reading score', y='writing score', title='Scatter Plot of reading score and writing score percentages');
plt.show()
print("df.corr(numeric_only=true):        " , df.corr(numeric_only=True))
print("df.describe():                    " , df.describe())


print(" df['reading score'] :     " , df['reading score'])
print("  df['writing score']   :    ", df['writing score'])


y = df['reading score'].values.reshape(-1, 1)
X = df['writing score'].values.reshape(-1, 1)
print("y :  " , y)
print("X :   " , X)
print(df['reading score'].values) 
print(df['reading score'].values.shape)
print(X.shape) 
print(X) 
SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)


print(X_train) 
print(y_train)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
def calc(slope, intercept, readingscore):
    return slope*readingscore+intercept

score = calc(regressor.coef_, regressor.intercept_, 90)
print(score) 
score = regressor.predict([[90]])
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