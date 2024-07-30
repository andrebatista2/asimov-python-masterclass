from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", page_title="Book Reviews")
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

books = df_top100_books['book title'].unique() # Traz todos os livros de forma única em forma de lista
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews = df_reviews[df_reviews["book name"] == book]

# O iloc retorna apenas o valor desejado de dentro da lista do DataFrame do Pandas
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"US$ {df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Rating", value=book_rating)

with col2:
    st.metric(label="Price", value=book_price)

with col3:
    st.metric(label="Year of Publication", value=book_year)

st.divider() # Mesmo que o <hr>

if df_reviews.empty:
    st.markdown(
        r"""
            <div style="display: flex; justify-content: center;">
                <h3>No Reviews Found</h3>
            </div>
        """,
        unsafe_allow_html=True
    )

for df_review in df_reviews.values:
    messages = st.chat_message(f"{df_review[4]}")
    messages.write(f"**{df_review[2]}**")
    messages.write(df_review[5])
