import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def summarize(df, stat):
    dat = df.drop(['Political_Party'], axis = 1)
    result = dat.melt(id_vars=['Date'], var_name='Variable', value_name='Value')
    vars = df.drop('Date', axis=1)
    if stat == 'mean':
        return vars.mean()
    elif stat == 'median':
        return vars.median()
    elif stat == 'max':
        return result.loc[result.groupby('Variable')['Value'].idxmax()]
    elif stat == 'min':
        return result.loc[result.groupby('Variable')['Value'].idxmin()]

def correlation(df, ax):
    edit = df.drop(['Date','Political_Party'], axis=1)
    corr = edit.corr()
    matrix = np.triu(corr)
    cmap = sns.diverging_palette(100, 7, s=75, l=40,
                            n=5, center="light", as_cmap=True)
    sns.heatmap(corr, mask=matrix, center=0, annot=True,
            fmt='.2f', square=True, cmap=cmap, ax = ax)

def time_series(fred, i):
    fig = px.line(fred, x = 'Date', y = i, title = f'{i} Over Time by President')
    fig.add_shape(
        type="line",
        x0="1939-01-01", x1="1939-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="blue", width=2, dash="dash") 
    )
    fig.add_shape(
        type="line",
        x0="1953-01-01", x1="1953-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="red", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="1961-01-01", x1="1961-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="blue", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="1969-01-01", x1="1969-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="red", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="1977-01-01", x1="1977-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="blue", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="1981-01-01", x1="1981-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="red", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="1993-01-01", x1="1993-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="blue", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="2001-01-01", x1="2001-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="red", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="2009-01-01", x1="2009-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="blue", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="2017-01-01", x1="2017-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="red", width=2, dash="dash")
    )
    fig.add_shape(
        type="line",
        x0="2021-01-01", x1="2021-01-01",  
        y0=min(fred[i]), y1=max(fred[i].dropna()),  
        line=dict(color="blue", width=2, dash="dash")
    )
    return fig


def party(fred):
    presidents = [
    {'start_date': '1939-01-01', 'end_date': '1953-01-19', 'party': 'Democrat'},
    {'start_date': '1953-01-20', 'end_date': '1961-01-19', 'party': 'Republican'},
    {'start_date': '1961-01-20', 'end_date': '1969-01-19', 'party': 'Democrat'},
    {'start_date': '1969-01-20', 'end_date': '1977-01-19', 'party': 'Republican'},
    {'start_date': '1977-01-20', 'end_date': '1981-01-19', 'party': 'Democrat'},
    {'start_date': '1981-01-20', 'end_date': '1993-01-19', 'party': 'Republican'},
    {'start_date': '1993-01-20', 'end_date': '2001-01-19', 'party': 'Democrat'},
    {'start_date': '2001-01-20', 'end_date': '2009-01-19', 'party': 'Republican'},
    {'start_date': '2009-01-20', 'end_date': '2017-01-19', 'party': 'Democrat'},
    {'start_date': '2017-01-20', 'end_date': '2021-01-19', 'party': 'Republican'},
    {'start_date': '2021-01-20', 'end_date': '2025-01-19', 'party': 'Democrat'}
    ]
    presidents_df = pd.DataFrame(presidents)
    presidents_df['start_date'] = pd.to_datetime(presidents_df['start_date'])
    presidents_df['end_date'] = pd.to_datetime(presidents_df['end_date'])
    fred['Date'] = pd.to_datetime(fred['Date'], errors='coerce')

    def get_party(date):
        for _, row in presidents_df.iterrows():
            if row['start_date'] <= date <= row['end_date']:
                return row['party']
        return None
    
    fredp = fred
    fredp['Political_Party'] = fredp['Date'].apply(get_party)
    return(fredp)