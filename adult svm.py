import pandas as pd
import matplotlib.pyplot as plt
col_names=['age', 'education', 'income', 'fnlwgt', 'capital.gain', 'capital.loss', 'occupation', 'relationship', 'income']
adultdata=pd.read_csv('archive (10)/adult.csv')
adultdata.head()
print(adultdata['age'].unique())
print(adultdata.shape)
print ( " Exploring the Dataset:  adultdata['age'].value_counts()) \n " , adultdata['age'].value_counts())
print("exploring the Dataset:  adultdata['age'].value_counts()) \n " , adultdata['age'].value_counts(normalize=True) )
adultdata['age'].plot.hist();
plt.show()
print("adultdata.describe().T   :    \n" , adultdata.describe().T )
import matplotlib.pyplot as plt
for col in adultdata.select_dtypes(include='number').columns:
    adultdata[col].plot.hist()
    plt.title(col)
    plt.show()
    gc= adultdata[col].plot.hist() 
    plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(adultdata, hue='age');
plt.show()

y = adultdata['age']
X = adultdata.drop('age', axis=1)
from sklearn.model_selection import train_test_split

SEED = 42

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = SEED)
print(X_train)
print(y_train)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]
X = pd.get_dummies(X, drop_first=True)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)
print(X_train.shape)
print(X_test.shape)
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
