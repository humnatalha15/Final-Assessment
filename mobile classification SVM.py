import pandas as pd
import matplotlib.pyplot as plt
col_names=['battery_power','price_range','three_g','four_g','dual_sim','fc','pc','ram']
mobiledata=pd.read_csv('mobile data classification 3/train.csv')
mobiledata.head()
print(mobiledata['price_range'].unique())
print(mobiledata.shape)
print(" Exploring the Dataset:  mobiledata['price_range'].value_counts()) \n " , mobiledata['price_range'].value_counts())
print("exploring the Dataset:  mobiledata['price_range'].value_counts()) \n " , mobiledata['price_range'].value_counts(normalize=True) )
mobiledata['price_range'].plot.hist();
plt.show()
print("mobiledata.describe().T   :    \n" , mobiledata.describe().T )
import matplotlib.pyplot as plt

for col in mobiledata.columns[:-1]:
    plt.title(col)
    gc= mobiledata[col].plot.hist() 
    gc.figure.show()
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(mobiledata, hue='price_range');
plt.show()
y = mobiledata['price_range']
X = mobiledata.drop('price_range', axis=1)
from sklearn.model_selection import train_test_split

SEED = 42

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = SEED)
xtrain_samples = X_train.shape[0]
xtest_samples = X_test.shape[0]
print(f'There are {xtrain_samples} samples for training and {xtest_samples} samples for testing.')
from sklearn.svm import SVC
svc = SVC(kernel='linear')
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