import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

# 나라별 cylinders 갯수 -> countplot 으로 그리기
g1 = sns.countplot(x="cylinders", data=mpg, hue='origin')

# 나라별 연도에 따른 생산 갯수 -> countplot 으로 그리기
g2 = sns.countplot(x="model_year", data=mpg, hue='origin')

# horsepower, mpg, weight 관계 -> pairplot

g3 = sns.pairplot(mpg, x_vars=["mpg", "cylinders", "horsepower"], hue='origin')
g1