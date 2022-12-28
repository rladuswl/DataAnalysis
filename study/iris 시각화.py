from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
iris = load_iris()

# 데이터 만들기
sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
petal_length = iris['data'][:, 2]
petal_width = iris['data'][:, 3]
target = iris['target']
targetName = iris['target_names']

tn = pd.Series(np.arange(150.))
tn[:50] = targetName[0]
tn[50:100] = targetName[1]
tn[100:150] = targetName[2]
# print(tn[49]) # 50번째
# print(tn[99]) # 100번째
# print(tn[149]) # 150번째
# print(tn) # 0~149, 총 150개 데이터

data = {'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
       'petal width (cm)': petal_width,
       'target': target,
       'targetName': tn}
frame = pd.DataFrame(data)
print(frame.head())

# scatter 그림 그리기
x1 = frame['sepal length (cm)']
y1 = frame['sepal width (cm)']

fig, ax = plt.subplots(1, 2, figsize=(13, 5))
ax[0].scatter(x1[:50], y1[:50], marker='o', c='r', label='setosa')
ax[0].scatter(x1[50:100], y1[50:100], marker='x', c='b', label='versicolor')
ax[0].scatter(x1[100:150], y1[100:150], marker='^', c='g', label='virginica')
ax[0].legend()
ax[0].set_xlabel('sepal length')
ax[0].set_ylabel('sepal width')

x2 = frame['petal length (cm)']
y2 = frame['petal width (cm)']

ax[1].scatter(x2[:50], y2[:50], marker='o', c='r', label='setosa')
ax[1].scatter(x2[50:100], y2[50:100], marker='x', c='b', label='versicolor')
ax[1].scatter(x2[100:150], y2[100:150], marker='^', c='g', label='virginica')
ax[1].legend()
ax[1].set_xlabel('petal length')
ax[1].set_ylabel('petal width')