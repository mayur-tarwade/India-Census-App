import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.title('India Census 2011 Analysis')

#Dataset Import
df = pd.read_csv(r'C:\Users\tarwa\OneDrive\Desktop\Data Science\Projects\India_Census_App\Datasets\Indian_Census_2011')
list_of_States = list(df['State'].unique())
list_of_States.insert(0,'Overall India')

# Sex Ratio
df['Sex_Ratio'] = round((df['Female']/df['Male'])*1000)
df['Literacy_Rate'] = round((df['Literate']/df['Population'])*100)
df
pri_para = df.columns

# App Layout

st.sidebar.title('India Census Visualization')
st.sidebar.selectbox('Slect a State', list_of_States)
st.sidebar.selectbox('Slect Primary Parameter', pri_para)
st.sidebar.selectbox('Slect Secondary Parameter', list_of_States)
st.sidebar.button('Plot')




