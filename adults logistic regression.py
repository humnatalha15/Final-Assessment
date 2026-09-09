import pandas as pd
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'occupation', 'relationship', 'capital.gain', 'capital.loss', 'income']
pima = pd.read_csv("archive (10)/adult.csv")
feature_cols = ['age', 'workclass', 'fnlwgt', 'education','occupation','relationship','capital.gain','capital.loss']
X = pima[feature_cols] 
y = pima.income
import numpy as np
from sklearn.preprocessing import LabelEncoder
X=X.replace('?', np.nan)
X=X.dropna()
y=y[X.index]
X=pd.get_dummies(X,drop_first=True)
le=LabelEncoder()
y=le.fit_transform(y)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)
print(X_train)
print(y_train)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=16, max_iter=1000)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(" Model Evaluation using Confusion Matrix : " , cnf_matrix)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class_names=[0,1] 
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
plt.Text(0.5,257.44,'Predicted label');