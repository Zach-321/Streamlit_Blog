import numpy as np
import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from my_plots import *
import streamlit as st

@st.cache_data
def load_data():
    data = pd.read_csv('fred_data.csv')
    return data

data = load_data()

st.title('Presidents and the Economy')

with st.sidebar:
    options = st.multiselect('Choose variables to compare', data.columns[1:])
    input_name = st.text_input('Enter a Name:','Zachary')
    year_input =st.slider('Year', 1880, 2023, value = 2003)
    n_names = st.radio('Number of Names per Sex', [3,5,10,20])


comp = scatter(data,options)
st.plotly_chart(comp)
    

# tab1, tab2 = st.tabs(['Name', 'Year'])
# with tab1:
#     name_data = data[data['name']== input_name].copy()
#     #fig = px.line(name_data, x = 'year', y = 'count', color = 'sex')
#     name_output = name_trend_plot(name_data, input_name)
#     #st.plotly_chart(fig)
#     st.plotly_chart(name_output)

# with tab2:
#     fig2 = top_names_plot(data, year = year_input, n = n_names)
#     st.plotly_chart(fig2)

#     st.write('Unique Names Table')
#     output = unique_names_summary(data, year_input)
#     st.dataframe(output)

# with st.expander('Feedback', icon  = '🤔'):
#     st.text('How would you rate your experience?')
#     face = st.feedback('faces')
#     if face is not None:
#         if face == 0:
#             st.text('Lying is a sin!')
#         elif face == 1:
#             st.text('Are you sure?')
#         elif face == 2:
#             st.text('That\'s it?')
#         elif face == 3:
#             st.text('Just pick the happiest face')
#         elif face == 4:
#             st.text('Thank you')
