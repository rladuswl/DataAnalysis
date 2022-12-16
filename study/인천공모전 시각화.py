import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns
import json
import numpy as np

filename = '10.[EXCEL]인천맛집_관광수용태세정보_무장애관광정보.xlsx'

df = pd.read_excel(filename)
df

# 어느 구에 맛집이 가장 많은지 (가장 활성화 되어있는지)
incheon = df[['카테고리 뎁스2', '시군구명', 'x좌표', 'y좌표']]
incheon.columns = ['카테고리', '시군구명', '경도', '위도']
incheon

# 구 / 카테고리 별 분포

# ---------

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'

plt.figure(figsize=(12, 10))
sns.countplot(y=incheon['카테고리'], order=incheon['카테고리'].value_counts().index)
plt.yticks(fontsize=12)
plt.title('인천시 업종별 개수')
plt.show()

# ---------

# obj = pd.Series(incheon['시군구명'])
# obj.unique()

count_data = incheon.groupby('시군구명').count().reset_index()
count_data

pd.DataFrame(count_data, columns=['시군구명', '개수'])
c = count_data[['시군구명', '카테고리']]
c

# ---------

# obj = pd.Series(incheon['시군구명'])
# obj.unique()

count_data = incheon.groupby('시군구명').count().reset_index()
count_data

pd.DataFrame(count_data, columns=['시군구명', '개수'])
c = count_data[['시군구명', '카테고리']]
c