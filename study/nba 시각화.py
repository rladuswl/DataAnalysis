import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('nba.csv')

print('1. 읽은 데이터에서 나이 Series로 히스토그램을 그리기')
obj = pd.Series(df['Age'])
plt.hist(obj)
plt.xlabel('age')
plt.ylabel('count')
print()

print('2. 연봉이 가장 높은 사람의 정보를 출력하기')
top_salary = df.sort_values(ascending=False, by='Salary').head(1)
print('Name:', top_salary['Name'].values[0])
print('Team:', top_salary['Team'].values[0])
print('Position:', top_salary['Position'].values[0])
print('Age:', top_salary['Age'].values[0])
print('Salary:', top_salary['Salary'].values[0])
print()

# -----------------------------------------

print('3. 팀별로 평균연봉을 바형태로 나타내기')
grouped = df['Salary'].groupby(df['Team'])
grouped_mean = grouped.mean()
#print(grouped_mean.index.values)
#print(grouped_mean.values)
plt.bar(np.arange(grouped_mean.index.size), grouped_mean.values)  # grouped_mean.plot.bar() 사용해도 됨
plt.xlabel('Team')
plt.ylabel('Salary')
print()
top_salary['Name'].iloc[0]
top_salary['Name'].values[0]

print('4. 선수들의 출신 학교별로의 인원수를 나타내시오')
print(df['College'].groupby(df['College']).count())
print()

# -----------------------------------------

print('5. 선수들의 평균 연봉과 나이를 출력하시오')
print('Avg Age:', df['Age'].mean())
print('Avg Salary:', df['Salary'].mean())
print()

# -----------------------------------------

print('6. 포지션 별로 이름을 출력하시오')
p = df.groupby(df['Position'])['Name']
for index, Name in p:
    print(index)
    print(Name)
print()

