# -*- coding: utf-8 -*-
"""MNIST

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JRnAZed2Eu-tyw90Ko90SFl-x1V17ucz

FETCHING THE "MNIST" DATASET
"""

from sklearn.datasets import fetch_openml

mnist = fetch_openml("mnist_784")

mnist

x , y = mnist["data"] , mnist["target"]

x.shape

y.shape

y[69852]

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib

import matplotlib.pyplot as plt

random_digit = x[25000]

"""LET'S RESHAPE THE RANDOM DIGIT AS A 28 BY 28 ARRAY IN ORDER TO PLOT IT"""

random_digit_image = random_digit.reshape(28,28)

plt.imshow(random_digit_image, cmap=matplotlib.cm.binary, interpolation="nearest" )
plt.axis("off")

y[25000]

"""SPLITTING THE DATASET INTO "TRAINING" AND "TESTING" SETS."""

x_train , x_test = x[:60000], x[60000:]

y_train , y_test = y[:60000], y[60000:]

"""NOW WE SHUFFLE THE DATASET TO ENSURE THAT EACH DATA POINT CREATES AN "INDEPENDENT" CHANGE ON THE MODEL, WITHOUT BEING BIASED BY THE SAME POINTS BEFORE THEM."""

import numpy as np
shuffle_index = np.random.permutation(60000)
x_train , y_train = x_train[shuffle_index] , y_train[shuffle_index]

"""**TRAINING OUR CLASSIFICATION ML MODEL**

**Model 1. Logistic Regression**
"""

from sklearn.linear_model import LogisticRegression

lmodel = LogisticRegression()
lmodel.fit(x_train, y_train)

lmodel.predict([x[25000]])

lmodel.predict([x[69852]])

"""**CALCULATING THE ACCURACY SCORE OF OUR MODEL**"""

from sklearn.metrics import accuracy_score,confusion_matrix
print(accuracy_score(y_train,lmodel.predict(x_train)))
print(accuracy_score(y_test,lmodel.predict(x_test)))

print(confusion_matrix(y_train,lmodel.predict(x_train)))
print(confusion_matrix(y_test,lmodel.predict(x_test)))

"""**Creating a "5" Detector**"""

y_train = y_train.astype(np.int8)
y_test = y_test.astype(np.int8)
y_train_5 = (y_train==5)
y_test_5 = (y_test==5)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(tol = 0.1, solver='lbfgs')
clf.fit(x_train, y_train_2)

clf.predict([random_digit])

from sklearn.model_selection import cross_val_score
a = cross_val_score(clf, x_train, y_train_2, cv=3, scoring="accuracy")
a.mean()

