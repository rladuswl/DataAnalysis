import seaborn as sns
import pandas as pd

df = pd.read_csv('nba.csv')
df
df.loc[(df['Team'] == 'Boston Celtics') | (df['Team'] == 'Utah Jazz')][['Age', 'Salary', 'Position', 'Team']]

# 1번

# 팀 : Milwaukee Bucks, New Orleans Pelicans
two_team = df.loc[(df['Team'] == 'Milwaukee Bucks') | (df['Team'] == 'New Orleans Pelicans')]
tt = two_team[['Age', 'Salary', 'Team', 'Position']]
tt
# Milwaukee Bucks와 New Orleans Pelicans 팀으로 추출한 결과이다. 그래프로 보기 전, 표를 통해 대략적으로 예상해보았을 때 나이는 20대 중후반이 많아 보이고 각 값마다 연봉은 차이가 커보인다.

# 2번

sns.set_theme(style="white")
g = sns.boxplot(x="Age", y="Salary", hue="Position", data=tt)
g

# 2번 요인플롯 형태의 그래프를 보면 x축은 나이(Age)이고 y축은 연봉(Salary)이다. 이를 Position 5종류로 나누어 그래프가 형성되었다. 또한, hue 인자에 Position이라는 구분값을 넣어 범주를 색상으로 표현하였다.
#
# 가장 긴 녹색(SG) 박스플롯
# 나이 27살에 차이가 뚜렷하게 분포되어있고, 그 중 25%는 연봉이 대략 4000000, 중앙값은 대략 8000000, 75%는 12000000 정도이다. 또한 연봉의 최소는 0보다 살짝 높고, 최대는 거의 16000000에 가깝게 분포되어 있다. 27살에서 최소와 최대값의 차이 정도가 가장 크기 때문에 위 그래프처럼 길게 그려졌다고 분석해볼 수 있다.
# 두번째로 긴 주황색(PG) 박스플롯
# 나이 25살에서 최소 연봉과 최대 연봉의 차이가 두번째로 크다고 볼 수 있다. 최소는 2000000이 조금 안되는 값이고, 중앙값은 6000000, 최대는 10000000와 12000000 사이이다. 또한 25%까지는 2000000과 4000000사이에, 75%는 8000000 조금 넘는 값에 분포되어 있음을 알 수 있다.
# 세번째로 긴 빨간색(PF) 박스플롯
# 나이 23살에서 최소와 최대의 차이가 세번째로 크게 분포되어 있다. 최소값은 0과 2000000 사이, 중앙값은 대략 4000000, 최대값은 6000000과 8000000 사이 이다. 25%까지는 2000000과 4000000 사이, 75%까지는 6000000 조금 안되는 연봉이 나타남을 알 수 있다.
# 네번째로 긴 파란색(SF) 박스플롯
# 나이 21살에서 연봉 최소와 최대 사이의 간격이 많이 줄어들었다. 최소는 2000000이 조금 안되는 값, 최대는 2000000이 조금 넘는 값으로 볼 수 있다. 나이 21살의 연봉 분포가 2000000 보다 조금 크고 작은 언저리에 위치함을 알 수 있다.
# 마지막 보라색(C) 박스플롯
# 위의 4개 Position과 다르게, 특별히 큰 차이를 나타내는 나이가 없다. 즉 C에 속하는 나이들은 전부 다를 것이고, 나이와 연봉에 맞는 데이터들이 점처럼 좌표에 찍혀 있음을 알 수 있다.
# 나이별 연봉에 대한 최대와 최소 차이를 쉽게 알 수 있고, 중앙값 또한 표시가 되어있어 한눈에 알아볼 수 있다. 결론적으로 27살 SG 포지션의 연봉 차이 분포가 가장 크며, C 포지션이 가장 작은 것을 알 수 있다. 27살의 연봉이 가장 높고, SG 포지션이 대체로 연봉을 높게 받음을 분석해볼 수 있다. 또한 C 포지션의 연봉은 다양하게 분포되어 있고, SF 포지션의 연봉은 대략적으로 가장 적게 나타난다.

sns.jointplot(x="Age", y="Salary", data=tt, kind='reg');

# 3번은 나이별 연봉에 대한 선형회귀선이 표시된 그래프이다. X축이 나이이고 Y축이 연봉을 나타내며, 나이와 연봉에 맞게 모든 데이터가 좌표점에 찍혀 산점도로 나타내고 있다. 따라서 나이와 연봉 두 컬럼에 대한 값의 분포라고 볼 수 있다. 나이와 연봉의 분포에 따라 회귀선이 표시되었으며, 값들은 회귀선 아래쪽에 더 많이 분포되어 있다.
#
# 가로의 막대 형식 그래프를 보면, 나이대별 분포를 알 수 있다. 26~28살 사이의 데이터가 가장 많고 그 다음으로 22, 24, 30 이 뒤를 이으며 대략 20살 즈음의 데이터가 가장 적다. 따라서 나이는 최소와 최대에 적게 분포되어 있고, 중앙값의 나이에 가장 값이 많은 것을 알 수 있다.
#
# 세로의 막대 형식 그래프를 보면, 연봉별 분포를 알 수 있다. 연봉 0~2000000 조금 넘는 구간의 값이 가장 많고, 그 다음으로 2000000과 4000000사이, 그 다음 8000000 .. 이렇게 분포되어 있다. 연봉의 값이 커질수록 그 값의 개수는 줄어드는 것을 볼 수 있다.
#
# 따라서 대체적으로 연봉은 0과 6000000사이, 나이는 25과 29살 사이에 값이 많이 분포되어 있다.

with sns.axes_style('white'):
    g = sns.catplot(x="Age", data=tt, aspect=4.0, kind='count',
                       hue='Position')
# 4번은 나이별 5개의 Position 분포를 나타낸다.
#
# 19살 SG 포지션만 존재한다. 그 수는 1명이다. 따라서 전체 데이터에서 10대는 SG 포지션에 존재하는 한 명 뿐이다.
#
# 21살 SF, PG, PF 포지션에만 존재한다. SF에서 2명, 나머지에서 1명씩 총 3명이 존재한다.
#
# 23살 SG, PF 포지션에만 존재한다. PF에서 2명, SG에서 1명 총 3명이 존재한다.
#
# 24살 PG, SG 포지션에만 존재한다. 각각 1명씩 총 2명 존재한다.
#
# 25살 C를 제외한 모든 포지션에 존재한다. 총 6명으로 25살이라는 값이 포지션에 고루 분포되어 있음을 알 수 있다.
#
# 26살 SF, SG, C 포지션에만 존재한다. 각각 1명씩 총 3명이 존재한다.
#
# 27살 PG, SG, C 포지션에만 존재한다. 25살과 마찬가지로 PG와 SG의 분포가 높게 나타난다.
#
# 28살 PG를 제외한 모든 포지션에 존재한다. 총 4명으로 여러 포지션에 고루 존재한다.
#
# 29살 SG를 제외한 모든 포지션에 존재한다. 마찬가지로 여러 포지션에 고루 존재하는 편이다.
#
# 30살 PG 포지션에만 존재한다. 여기서부터 눈에 띄게 막대 그래프가 줄어들었다. PG 포지션 하나에만 1명 존재한다.
#
# 31살 C 포지션에만 존재한다. 30살과 마찬가지로 C 포지션에만 딱 1명 있으며 분포가 눈에 띄게 줄었다.
#
# 32살 SF 포지션에만 존재한다. 이 또한 마찬가지이다.
#
# 한눈에 봐도 25살부터 29살까지의 분포는 많이 보이지만, 10대와 30대 분포는 현저히 적게 나타난다. 총 카운트 수도 마찬가지로 20대에 더 높은 결과를 나타냄을 알 수 있다.
