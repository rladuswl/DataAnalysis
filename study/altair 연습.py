import altair as alt
import pandas as pd
import plotly as px

wide_df = px.data.medals_wide()
wide_df

chart1 = alt.Chart(wide_df).mark_bar().encode(
    x='nation',
    y='gold'
)

chart2 = alt.Chart(wide_df).mark_bar().encode(
    x='nation',
    y='silver'
)

chart3 = alt.Chart(wide_df).mark_bar().encode(
    x='nation',
    y='bronze'
)

alt.hconcat(chart1, chart2, chart3)
# chart1 | chart2 | chart3