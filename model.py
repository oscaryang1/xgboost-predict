
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn import preprocessing, metrics, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import xgboost as xgb


data_train = pd.read_csv(r"junyi.csv")


cols = ['bmi','sex','edu','race','diabetes','smoke','cholesterol_mg','vitamin_K_mcg','caffeine_mg','high','low']
x = data_train[cols].values
y = data_train['score'].values


X_train, y_train, = x,y
ss_X = preprocessing.MinMaxScaler()
ss_Y = preprocessing.MinMaxScaler()

X_train_scaled = ss_X.fit_transform(X_train)
y_train_scaled = ss_Y.fit_transform(y_train.reshape(-1, 1))


print(y_train_scaled)
X_validation_scaled = X_train_scaled
y_validation_scaled = y_train_scaled

print(X_validation_scaled[0:2])

xgb_model = xgb.XGBRegressor(max_depth=10,
                             learning_rate=0.1,
                             n_estimators=50,
                             objective='reg:linear',
                         
                             )

xgb_model.fit(X_train_scaled, y_train_scaled)

y_validation_pred = xgb_model.predict(X_validation_scaled)

xgb_model.save_model('D:/model.json')



