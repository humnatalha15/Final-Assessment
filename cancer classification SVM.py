import pandas as pd
import matplotlib.pyplot as plt
cancer = pd.read_csv("classification 1/data.csv")
cancer.head()
print(cancer['radius_mean'].unique())
print(cancer.shape)
print ( " Exploring the Dataset:  cancer['radius_mean'].value_counts()) \n " , cancer['radius_mean'].value_counts()) , cancer ['radius_mean'].plot.hist();
plt.show()
print("cancer.describe().T   :    \n" , cancer.describe().T )
import matplotlib.pyplot as plt

for col in cancer.columns:
    if col!='diagnosis':
        plt.figure()
        cancer[col].plot.hist(bins=20)
        plt.title(col)
        plt.show()
        gc= cancer[col].plot.hist() 
        gc.figure.show()
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(cancer, hue='radius_mean');
plt.show()
cancer = cancer.drop(columns=['Unnamed: 32'])
y = cancer['radius_mean']
X = cancer.drop('radius_mean', axis=1)
y = cancer['diagnosis']
X = cancer.drop(columns=['diagnosis', 'id'], errors='ignore')
X = X.drop(columns=['Unnamed: 32'], errors='ignore')
X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(X.median())
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.svm import LinearSVC
svc = LinearSVC(max_iter=5000)
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_test,y_pred)
gg=sns.heatmap(cm, annot=True, fmt='d').set_title('Confusion matrix of linear SVM') # fmt='d' formats the numbers as digits, which means integers
gg.figure.show() 
print(classification_report(y_test,y_pred))