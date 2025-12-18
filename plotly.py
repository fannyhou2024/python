import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
df = px.data.iris()
print(df.head())
fig = px.scatter(df, x='sepal_width',
y='sepal_length',
color='species',
size='petal_length',
hover_data=['petal_width'])
fig.show()
