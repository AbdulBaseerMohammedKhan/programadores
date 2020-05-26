from xgboost import XGBClassifier
import pandas as pd
from sklearn.metrics import accuracy_score

train = pd.read_csv('final_train.csv') #27000 patients

train_copy = train.groupby('Patient_id').mean().fillna(train.mean())
train_copy['SepsisLabel'][train_copy['SepsisLabel']!=0] = 1
x = train_copy.drop(['SepsisLabel'],axis = 1)
y = train_copy['SepsisLabel']

xgb = XGBClassifier()
xgb.fit(x,y)

test = pd.read_csv('train_patient.csv')  #22000 patients

test_copy = test.groupby('Patient_id').mean().fillna(test.mean())
test_copy['SepsisLabel'][test_copy['SepsisLabel']!=0] = 1

x1 = test_copy.drop(['SepsisLabel'],axis = 1)
y1 = test_copy['SepsisLabel']
#c = test_copy["Patient_id"]




y_pred = xgb.predict(x)
print("Train Accuracy: ",accuracy_score(y_pred, y))


y1_pred = xgb.predict(x1)
print("Test Accuracy: ",accuracy_score(y1_pred, y1))
print(y1_pred)
print(y1)
print(x1)