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
st.write('Book Reviews')
