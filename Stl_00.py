import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.title('Hello World Anirach')
st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)
placeholder = st.empty()
status = st.radio('Choose your status:', ['Active', 'Inactive'])

if status == 'Active':
    placeholder.text('User is active')

st.write('This is a simple example of Streamlit web application!.')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
