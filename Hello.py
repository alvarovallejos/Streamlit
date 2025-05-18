import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Quick Data Explorer", layout="wide")

# Title
st.title("📊 Quick Data Explorer")

# Load sample dataset from Seaborn
dataset_names = ["tips", "titanic", "iris", "penguins"]
selected_dataset = st.selectbox("Choose a dataset", dataset_names)

@st.cache_data  # Cache the data load
def load_data(name):
    return sns.load_dataset(name)

df = load_data(selected_dataset)

# Show dataset info
st.subheader("Dataset Preview")
st.write(f"Shape: {df.shape} (rows, columns)")
st.dataframe(df.head())

# Basic statistics
st.subheader("Basic Statistics")
st.write(df.describe())

# Simple visualization
st.subheader("Data Visualization")

col1, col2 = st.columns(2)

with col1:
    x_axis = st.selectbox("X-axis", df.columns)
with col2:
    y_axis = st.selectbox("Y-axis", df.columns)

chart_type = st.radio("Chart type", ["Scatter", "Line", "Bar"])

fig, ax = plt.subplots()
if chart_type == "Scatter":
    sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
elif chart_type == "Line":
    sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
else:
    sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)

st.pyplot(fig)

# Show raw data if needed
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(df)