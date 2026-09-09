import pandas as pd
col_names=['blue','clock_speed','dual_sim','fc','pc','four_g','battery_power', 'price_range']
pima=pd.read_csv('mobile data classification 3/train.csv')
feature_cols = ['blue', 'clock_speed', 'dual_sim','fc','pc','four_g','battery_power']
X = pima[feature_cols] 
y = pima.price_range
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=16,max_iter=1000)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(" Model Evaluation using Confusion Matrix : " , cnf_matrix)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class_names=[0,1] # name  of classes
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
target_names = ['high price', 'low price', 'medium low', 'medium high']
print(classification_report(y_test, y_pred, target_names=target_names))
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()