import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

col_names = ['age', 'workclass', 'education', 'capital.gain', 'capital.loss', 'fnlwgt', 'income', 'occupation', 'relationship']
pima = pd.read_csv("archive (10)/adult.csv")
#split dataset in features and target variable
feature_cols = ['age', 'workclass', 'education', 'capital.gain','capital.loss','fnlwgt', 'occupation', 'relationship']
X = pima[feature_cols] 
y = pima.income
X=pd.get_dummies(X, drop_first=True)
import numpy as np
X=X.replace('?', np.nan)
X=X.dropna()
y=y[X.index]
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
print(X_train)
print(y_train)
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = X.columns,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('adultV1.png')
Image(graph.create_png())


