import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_parquet('./unemployment_rate.parquet')

st.title('Estimated Employment Analysis (Covid 2019-2020)')

# Statewise
st.markdown('## State Wise Comparative Analysis')

state_options = df['Region'].unique().tolist()

state = st.multiselect("Choose the state", state_options, ['Bihar', 'West Bengal'])

df = df[df['Region'].isin(state)]

fig = px.bar(data_frame=df, x='Region', y='Estimated Employed', color='Region', animation_frame='Date', animation_group='Region', range_y=[85000, 60000000])

fig.update_layout(width=800, height=700)

st.plotly_chart(fig)


# urban regionwise 
df = pd.read_parquet('./unemployment_rate.parquet')
st.write('---')
st.markdown('## Urban Region Wise Assessment')

region_option = df['Regional'].unique().tolist()
region = st.selectbox("Choose the Region", region_option)

df = df[(df['Regional']==region) & (df['Area']=='Urban')]

fig = px.bar(data_frame=df, x='Region', y='Estimated Employed', color='Region', animation_frame='Date', animation_group='Region', range_y=[85000, 60000000])
fig.update_layout(width=800, height=700)

st.plotly_chart(fig)