import pandas as pd
col_names = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'radius_se', 'texture_se']
pima = pd.read_csv("classification 1/data.csv")
feature_cols = ['id', 'radius_mean', 'texture_se', 'texture_mean','perimeter_mean','area_mean','smoothness_mean', 'radius_se']
X = pima[feature_cols] 
y = pima.diagnosis
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)
print(X_train)
print(y_train)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=16)
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
from sklearn.metrics import classification_report
target_names = ['without cancer', 'with cancer']
print(classification_report(y_test, y_pred, target_names=target_names))
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba, pos_label='M')
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

input("Wait for me....")
