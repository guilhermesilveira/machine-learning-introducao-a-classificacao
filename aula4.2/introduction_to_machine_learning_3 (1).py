# -*- coding: utf-8 -*-
"""Introduction to Machine Learning - 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1femZm6uBR1H75XvsBQdtSuXQcFqZazSG
"""

!pip install seaborn==0.9.0

import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
data  = pd.read_csv(uri)
data.head()

swap = {
    0 : 1,
    1 : 0
}
data['finished'] = data.unfinished.map(swap)
data.head()

data.tail()

data.finished.hist()

import seaborn as sns

sns.scatterplot(x="expected_hours",y="price",data=data)

sns.scatterplot(x="expected_hours",y="price",
                hue="finished",
                data=data)

"""# Trying to run our basic model"""

x = data[["expected_hours","price"]]
y = data["finished"]

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np

SEED = 20
np.random.seed(SEED)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25,
                                                        stratify=y)
print("Train set lenght %d and test set lenght %d" % (len(train_x), len(test_x)))

model = LinearSVC()
model.fit(train_x, train_y)
predictions = model.predict(test_x)

accuracy = accuracy_score(test_y, predictions) * 100
print("Accuracy %.2f%%"% accuracy)

baseline_predictions = np.ones(540)
baseline_accuracy = accuracy_score(test_y, guilherme_predictions) * 100
print("Baseline Accuracy %.2f%%"% baseline_accuracy)

"""# Exploring the test"""

sns.scatterplot(x=test_x.expected_hours, y=test_x.price,
                hue=test_y)

x_min = test_x.expected_hours.min()
x_max = test_x.expected_hours.max()
y_min = test_x.price.min()
y_max = test_x.price.max()
print(x_min, x_max, y_min, y_max)

pixels = 100
x_axis = np.arange(x_min, x_max, (x_max - x_min) / pixels)
y_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(x_axis, y_axis)
points = np.c_[xx.ravel(), yy.ravel()]

Z = model.predict(points)
Z = Z.reshape(xx.shape)
Z.shape
Z

import matplotlib.pyplot as plt

plt.contourf(xx, yy, Z, alpha=0.1)
plt.scatter(test_x.expected_hours, test_x.price, c=test_y, s=1)

"""# Using non linear models"""

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

SEED = 20
np.random.seed(SEED)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25,
                                                        stratify=y)
print("Train set lenght %d and test set lenght %d" % (len(train_x), len(test_x)))

model = SVC()
model.fit(train_x, train_y)
predictions = model.predict(test_x)

accuracy = accuracy_score(test_y, predictions) * 100
print("Accuracy %.2f%%"% accuracy)

import matplotlib.pyplot as plt

def plot_decision_boundary(model):
  x_min = test_x.expected_hours.min()
  x_max = test_x.expected_hours.max()
  y_min = test_x.price.min()
  y_max = test_x.price.max()

  pixels = 100
  x_axis = np.arange(x_min, x_max, (x_max - x_min) / pixels)
  y_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

  xx, yy = np.meshgrid(x_axis, y_axis)
  points = np.c_[xx.ravel(), yy.ravel()]

  Z = model.predict(points)
  Z = Z.reshape(xx.shape)

  plt.contourf(xx, yy, Z, alpha=0.3)
  plt.scatter(test_x.expected_hours, test_x.price, c=test_y, s=1)

plot_decision_boundary(model)

"""# Let's use a Scaler"""

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

SEED = 20
np.random.seed(SEED)

raw_train_x, raw_test_x, train_y, test_y = train_test_split(x, y, test_size=0.25,
                                                        stratify=y)
print("Train set lenght %d and test set lenght %d" % (len(train_x), len(test_x)))

scaler = StandardScaler()
scaler.fit(raw_train_x)
train_x = scaler.transform(raw_train_x)
test_x = scaler.transform(raw_test_x)

model = SVC()
model.fit(train_x, train_y)
predictions = model.predict(test_x)

accuracy = accuracy_score(test_y, predictions) * 100
print("Accuracy %.2f%%"% accuracy)

import matplotlib.pyplot as plt

def plot_decision_boundary(model):
  data_x = test_x[:,0]
  data_y = test_x[:,1]
  
  x_min = data_x.min()
  x_max = data_x.max()
  y_min = data_y.min()
  y_max = data_y.max()

  pixels = 100
  x_axis = np.arange(x_min, x_max, (x_max - x_min) / pixels)
  y_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

  xx, yy = np.meshgrid(x_axis, y_axis)
  points = np.c_[xx.ravel(), yy.ravel()]

  Z = model.predict(points)
  Z = Z.reshape(xx.shape)

  plt.contourf(xx, yy, Z, alpha=0.3)
  plt.scatter(data_x, data_y, c=test_y, s=1)

plot_decision_boundary(model)

