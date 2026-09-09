import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('australia classification/weatherAUS.csv')
X=df.drop('Rainfall', axis=1)
Y=df['Rainfall']
import numpy as np
from sklearn.preprocessing import LabelEncoder
X=X.replace('?', np.nan)
X=X.dropna()
y=Y[X.index]
X=pd.get_dummies(X,drop_first=True)
le=LabelEncoder()
y=le.fit_transform(y)
print(df['Rainfall'].unique())
print(df.shape)
print ( " Exploring the Dataset:  df['Rainfall'].value_counts()) \n " , df['Rainfall'].value_counts())
print ( " Exploring the Dataset:  df['Rainfall'].value_counts()) \n " , df['Rainfall'].value_counts(normalize=True) )

print("df.describe().T   :    \n" , df.describe().T )
import matplotlib.pyplot as plt
numeric_cols=df.select_dtypes(include='number').columns

for col in numeric_cols:
    plt.figure()
    df[col].plot.hist()
    plt.title(col)
    plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

plot_df=df[['MinTemp', 'MaxTemp','Humidity3pm','Rainfall']].copy()
sns.pairplot(plot_df, hue='Rainfall')
plt.show()

df = df.dropna(subset=['RainTomorrow'])

X = df.drop(columns=['Date', 'RainTomorrow'])
y = df['RainTomorrow']
X = pd.get_dummies(X, drop_first=True)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
X = pd.DataFrame(imputer.fit_transform(X),columns=X.columns)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train NaN:", X_train.isna().sum().sum())
print("y_train NaN:", y_train.isna().sum())
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
from sklearn.svm import LinearSVC

svc = LinearSVC(max_iter=5000)
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
plt.title('Confusion matrix of linear SVM')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print(classification_report(y_test, y_pred))