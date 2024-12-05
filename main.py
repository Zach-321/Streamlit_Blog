import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data():
    data = pd.read_csv('fred_data.csv')
    return data

data = load_data()

st.title('Presidents and Economic Data')

with st.sidebar:
    time = st.selectbox('Choose 1 Variable for Time Series Analysis', data.columns[1:])
    options = st.multiselect('Choose at Least 1 Variable for Comparison', data.columns[1:])
    summary = st.radio('Choose a Summary Statistic', ['mean','median', 'max', 'min'])


tab1, tab2, tab3 = st.tabs(['Time Series','Plots', 'Summaries'])

with tab1:
    fig = time_series(data,time)
    st.plotly_chart(fig)

with tab2:
    try:
        colors = {'Democrat' : 'blue', 'Republican': 'red'}
        fig = sns.pairplot(party(data),vars = options, hue = 'Political_Party', palette = colors)
        st.pyplot(fig)
    except:
        st.text('Please select at least 1 variable')
    fig, ax = plt.subplots()
    correlation(data, ax)
    st.pyplot(fig)

with tab3:
    sum = summarize(data,summary)
    st.table(sum)

with st.expander('Feedback', icon  = '🤔'):
    st.text('How would you rate your experience?')
    face = st.feedback('faces')
    if face is not None:
        if face == 0:
            st.text('Lying is a sin!')
        elif face == 1:
            st.text('Are you sure?')
        elif face == 2:
            st.text('That\'s it?')
        elif face == 3:
            st.text('Just pick the happiest face')
        elif face == 4:
            st.text('Thank you')
