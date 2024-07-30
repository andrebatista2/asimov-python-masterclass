import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(layout="wide", page_title="Trending Books")
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        
        #MainMenu { 
            visibility: hidden; 
        }
        
        .stDeployButton { 
            display:none; 
        }
        
        footer { 
            visibility: hidden; 
        }
        
        #stDecoration { 
            display:none; 
        }
    </style>
""", unsafe_allow_html=True)

df_reviews = pd.read_csv(Path(__file__).parents[1] / 'datasets/customer reviews.csv')
df_top100_books = pd.read_csv(Path(__file__).parents[1] / 'datasets/Top-100 Trending Books.csv')

price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()

max_price = st.sidebar.slider("Book Prices", price_min, price_max, price_max / 2)

# Retorna os dados do Pandas de acordo com o critério dentro dos colchetes
df_top100_books[df_top100_books['book price'] <= max_price]

col1, col2 = st.columns(2)
with col1:
    fig = px.bar(df_top100_books['year of publication'].value_counts())
    st.plotly_chart(fig)

with col2:
    fig2 = px.histogram(df_top100_books['book price'])
    st.plotly_chart(fig2)
