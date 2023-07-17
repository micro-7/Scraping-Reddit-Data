import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os
SAVE_LOC = "collected_data/"

def load_files():
    files = os.listdir(SAVE_LOC)
    return [SAVE_LOC+file for file in files]

st.title("Collected Data")
sfile = st.selectbox('Select a file', load_files())

df = None
if sfile.endswith('.csv'):
    df = pd.read_csv(sfile)
    if 'comment' in sfile:
        st.dataframe(df, use_container_width=True)
        try:
            fig1 = px.area(df,x='id', y='score', hover_name='comment')
            st.plotly_chart(fig1, use_container_width=True)
            fig2 = px.area(df,x='id', y=['ups','downs'], hover_name='comment')
            st.plotly_chart(fig2, use_container_width=True)
            authors = df.groupby('author')['ups'].sum().reset_index()
            fig3 = px.area(authors, x='author', y='ups')
            st.plotly_chart(fig3, use_container_width=True)
        except Exception as e:
            st.error(e)
    else:
        try:
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df,y='score')
            try:st.bar_chart(df, y='num_comments')
            except:pass
            try:comdf = df.sort_values('num_comments').tail(10)
            except:pass
            try:
                fig2 = px.bar(comdf, x='id', y='num_comments', title="Top 10 comments count", log_y=True, hover_name='title', height=500)
                st.plotly_chart(fig2, use_container_width=True)
            except:pass
        except Exception as e:
            st.error(e)
elif sfile.endswith('.xlsx'):
    df = pd.read_excel(sfile)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df,x='title', y='score')
    st.bar_chart(df, x='title', y='num_comments')
    comdf = df.sort_values('num_comments').tail(10)
    fig2 = px.bar(comdf, x='id', y='num_comments', title="Top 10 comments count", log_y=True, hover_name='title', height=500)
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.write(sfile)