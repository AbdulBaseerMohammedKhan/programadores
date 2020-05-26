
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn.metrics import accuracy_score



train = pd.read_csv('output.csv')
train_copy = train.groupby('Patient_id').mean().fillna(train.mean())
train_copy['SepsisLabel'][train_copy['SepsisLabel']!=0] = 1
x = train_copy.drop(['SepsisLabel'],axis = 1)
y = train_copy['SepsisLabel']





model = Sequential()
model.add(Dense(60,input_dim = 41,activation='relu'))
model.add(Dense(105,activation = 'relu'))
model.add(Dense(88,activation = 'relu'))
model.add(Dense(10,activation = 'relu'))
model.add(Dense(1,activation = 'sigmoid'))


model.compile(loss="binary_crossentropy",optimizer = "adam", metrics=['accuracy'])

model.fit(x,y,epochs=50,batch_size = 10)

scores = model.evaluate(x,y)
print("\n%s: %.2f%% " % (model.metrics_names[1],scores[1]*100))

test = pd.read_csv('train_patient.csv')

test_copy = test.groupby('Patient_id').mean().fillna(test.mean())
test_copy['SepsisLabel'][test_copy['SepsisLabel']!=0] = 1
x1 = test_copy.drop(['SepsisLabel'],axis = 1)
y1 = test_copy['SepsisLabel']

scores = model.evaluate(x1,y1)
print("\n%s: %.2f%% " % (model.metrics_names[1],scores[1]*100))





