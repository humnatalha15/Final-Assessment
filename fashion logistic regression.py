import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('archive (13)/fashion-mnist_train.csv')
X=df.drop('label', axis=1)
Y=df['label']
import numpy as np
from sklearn.preprocessing import LabelEncoder
X=X.replace('?', np.nan)
X=X.dropna()
Y=Y[X.index]
X=pd.get_dummies(X,drop_first=True)
le=LabelEncoder()
y=le.fit_transform(Y)
print(df['label'].unique())
print(df.shape)
print ( " Exploring the Dataset:  df['label'].value_counts()) \n " , df['label'].value_counts())
print ( " Exploring the Dataset:  df['label'].value_counts()) \n " , df['label'].value_counts(normalize=True) )

print("df.describe().T   :    \n" , df.describe().T)
import matplotlib.pyplot as plt
numeric_cols=df.select_dtypes(include='number').columns

for col in numeric_cols:
    plt.figure()
    df[col].plot.hist()

    plt.title(col)
    plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df, hue='label');
plt.show
from sklearn.model_selection import train_test_split

SEED = 42

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = SEED)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]
from sklearn.svm import LinearSVC

svc = LinearSVC(max_iter=5000)
svc.fit(X_train, y_train)

y_pred = svc.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d')
plt.title('Confusion matrix of Linear SVM')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print(classification_report(y_test, y_pred))

