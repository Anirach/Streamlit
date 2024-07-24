import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris

# Load the Iris dataset
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    return df

# Load data
df = load_data()

# Title of the app
st.title("Iris Dataset Visualization")

# Sidebar for user input
st.sidebar.header("Filter Options")
species_filter = st.sidebar.multiselect(
    "Select Species",
    options=df['species'].unique(),
    default=df['species'].unique()  # Default to all species
)

# Filter the DataFrame based on user selection
filtered_df = df[df['species'].isin(species_filter)]

# Create a scatter plot using Plotly
fig = px.scatter(
    filtered_df,
    x='sepal length (cm)',
    y='sepal width (cm)',
    color='species',
    title="Iris Sepal Dimensions",
    hover_data=['petal length (cm)', 'petal width (cm)'],
    labels={'species': 'Iris Species'}
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Display the filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_df)
