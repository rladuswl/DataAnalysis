# https://altair-viz.github.io/gallery/grouped_bar_chart.html

import seaborn as sns
import altair as alt
from vega_datasets import data

mpg = sns.load_dataset('mpg')
mpg

alt.Chart(mpg).mark_bar().encode(
    x='cylinders:O',
    y='sum(horsepower):Q',
    color='cylinders:N',
    column='origin:N'
)

# 1번 문제 차트해석
# 각 나라별 (europe, japan, usa) cylinder의 sum of horsepower를 그린 차트를 보면,
#
# 전반적인 차트를 보았을 때 usa의 horsepower가 높은 것을 확인할 수 있다.
#
# cylinder 3에서의 horsepower 합은 japan에서만 나타나고 있고, 4에서는 세 나라가 비슷하지만 europe, japan, usa 순으로 조금씩 차이가 난다. 5에서는 europe에서만 조금 보이고, 6에서는 usa가 europe, japan보다 상대적으로 높은 값을 나타냄을 알 수 있다. 마찬가지로 8에서도 usa에서 가장 높게 나타나면서 usa에만 존재한다.
#
# 결과적으로 usa의 cylinder 6과 8에서의 sum of horsepower가 월등히 높은 값을 나타내고 있지만, 3과 5에서의 sum of horsepower은 존재하지 않는다. europe과 japan은 비슷해보이지만, 전반적으로 japan의 horsepower 값이 조금 더 많은 것을 확인할 수 있다.

# https://altair-viz.github.io/gallery/step_chart.html

import altair as alt
from vega_datasets import data
import seaborn as sns

pl = sns.load_dataset('flights')
pl

ch1 = alt.Chart(pl).mark_line(
    interpolate='step-after'
).encode(
    x='year',
    y='passengers'
).transform_filter(
    alt.datum.month == 'Jan'
)

ch2 = alt.Chart(pl).mark_line(interpolate='step-after').encode(
    x='year',
    y='passengers'
).transform_filter(
    alt.datum.month == 'Aug'
)

ch1 | ch2