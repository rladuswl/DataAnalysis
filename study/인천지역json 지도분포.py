center = [37.431069510239944, 126.63483680503974]

m = folium.Map(location=center, zoom_start=10) # tiles='stamentoner'

geo_data = json.load(open('./TL_SCCO_SIG1.json', encoding='UTF-8'))

folium.Choropleth(geo_data=geo_data, data=c,
                   columns=('시군구명', '카테고리'),
                   key_on='feature.properties.SIG_KOR_NM',
                   fill_color='PuRd', legend_name='인천 맛집 분포도' ).add_to(m)
folium.LayerControl().add_to(m)
m