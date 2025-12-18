# import streamlit as st
# import plotly.express as px
# import plotly.io as pio
# # pio.renderers.default = "browser"
# df = px.data.iris()
# print(df.head())
# fig = px.scatter(df, x='sepal_width',
# y='sepal_length',
# color='species',
# size='petal_length',
# hover_data=['petal_width'])
# fig.show()

import plotly.express as px
import streamlit as st
import pandas as pd

# Load data
df = px.data.gapminder()

# Create figure
fig = px.scatter(df, x='year', y='lifeExp', color='continent')

# Use Streamlit's native command to show the plot
st.plotly_chart(fig)
