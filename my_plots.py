import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



def pairs(df, options):
    if len(options) == 0:
        return None
    fig = sns.pairplot(df[options])
    return fig


def summarize(df, stat):
    result = df.melt(id_vars=['Date'], var_name='Variable', value_name='Value')
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
    edit = df.drop('Date', axis=1)
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
