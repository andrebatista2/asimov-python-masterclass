import streamlit as st

st.set_page_config(layout="wide", page_title="Main")
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
st.markdown(
    r"""
        <h1> Welcome to Trending and Book Reviews! </h1>
        <br>
        <p>Choose an option at the left to begin!</p>
    """,
    unsafe_allow_html=True,
)
