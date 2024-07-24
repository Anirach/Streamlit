import streamlit as st
import pandas as pd
import plotly.express as px

# Load sample data
@st.cache
def load_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    return pd.read_csv(url)

df = load_data()

# Title of the app
st.title("Air Travel Time Series Plot")

# Display the dataframe
st.write("This chart shows the number of air passengers traveled in each month from 1949 to 1960.")
st.dataframe(df)

# Create a line chart using Plotly
fig = px.line(df, x="Month", y=df.columns[1:], title="Air Passenger Travel")
st.plotly_chart(fig, use_container_width=True)