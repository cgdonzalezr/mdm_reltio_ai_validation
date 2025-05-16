import streamlit as st
import altair as alt
import dataiku
import pandas as pd, numpy as np
import re

from datetime import datetime, timedelta
from dataiku import pandasutils as pdu

# import config


# Sidebar section for user interaction
with st.sidebar:

    # Display a logo image
    st.image("https://www.wexinc.com/wp-content/uploads/2023/04/Logo.svg")

    # Title for the application
    st.title('MDM/Reltio Validation')

    # Selectbox for choosing the main section
    st.selectbox("Select section", ["Synthetic Data Generation", "Validation"], key = "section", index = 0)
    

# Conditional section for Synthetic Data Generation steps
if st.session_state.section == 'Synthetic Data Generation':

    st.write("Hello world")    
