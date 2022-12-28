import pandas as pd
import folium
import matplotlib.pyplot as plt
import json
import numpy as np

df = pd.read_csv('./camping_loc.csv', encoding='CP949' )

geo_data = json.load(open('./TL_SCCO_CTPRVN.json', encoding='UTF-8'))
df

m = folium.Map(location=[38.011952, 128.542213], zoom_start=10)

for i in df.index:
    name = df.loc[i, '캠핑(야영)장명']
    lat = df.loc[i, '위도']
    lng = df.loc[i, '경도']
    marker= folium.Marker([lat,lng], popup=name).add_to(m)
m

# 제주특별자치도, 경기도, 강원도, 충청남도, 충청북도, 전라남도, 전라북도, 경상남도, 경상북도

df['주소']

# 맨 앞 주소 가져오기 ('~도' 외에도 주소의 데이터가 다양하여 '~시', '~군', '~면' 등이 있을 수도 있음 주의)
do1 = df['주소'].str.split(' ').str[0]
# print(do1)

# null 값 제거
do1.isnull().sum()
do2 = do1.dropna(axis=0)
# print(do2)

# 주소의 형태가 다양하므로 unique를 통해 확인
unique_lst = do2.unique()
unique_lst

# 해당 단어가 포함되는 경우를 적용하여 데이터를 뽑아 전처리 하기
jj = do2.str.contains('제주')
gg = do2.str.contains('경기')
gw = do2.str.contains('강원')
cn = do2.str.contains('충청남도|충남')
cb = do2.str.contains('충청북도|충북')
jn = do2.str.contains('전라남도|전남')
jb = do2.str.contains('전라북도|전북')
kn = do2.str.contains('경상남도|경남')
kb = do2.str.contains('경상북도|경북')

# x 값은 도
name = ['제주특별자치도', '경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도']
# y 값은 도별 등록된 야영장 개수
count_value = [do2[jj].count(), do2[gg].count(), do2[gw].count(), do2[cn].count(), do2[cb].count(), do2[jn].count(), do2[jb].count(), do2[kn].count(), do2[kb].count()]

plt.rc('font', family='Malgun Gothic') # 한글 깨짐 처리
plt.figure(figsize=(12,8))
plt.bar(name, count_value, color='green')
plt.title('도별 야영장 등록현황', fontsize=25)
plt.xlabel('도(행정구역)', fontsize=15)
plt.ylabel('야영장 등록현황', fontsize=15)

plt.show()

