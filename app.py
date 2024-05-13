import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


st.set_page_config(layout='wide')
st.title('India Census 2011 Analysis')

#Dataset Import
df = pd.read_csv(\Datasets\Indian_Census_2011')
list_of_States = list(df['State'].unique())
list_of_States.insert(0,'Overall India')

# Sex Ratio
df['Sex_Ratio'] = round((df['Female']/df['Male'])*1000)
df['Literacy_Rate'] = round((df['Literate']/df['Population'])*100)
df
pri_para = df.columns[2:]


# App Layout

st.sidebar.title('India Census Visualization')
selected_states = st.sidebar.selectbox('Slect a State', list_of_States)
primary = st.sidebar.selectbox('Slect Primary Parameter', pri_para)
secondary = st.sidebar.selectbox('Slect Secondary Parameter',pri_para)
plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_states == 'Overall India':
        # Plot graph for India using plotly mapbox function.
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=5,hover_name='District',size_max=35,
                  mapbox_style="carto-positron",width=1500,height=700)
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State']==selected_states]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=5,hover_name='District',size_max=35,
                  mapbox_style="carto-positron",width=1500,height=700)
        st.plotly_chart(fig, use_container_width=True)
        
