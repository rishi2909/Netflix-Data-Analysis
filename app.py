import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📺 Netflix Movies and TV Shows Dashboard")

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Show dataset
st.subheader("Dataset Overview")
st.dataframe(df.head())

# Sidebar filters
st.sidebar.header("Filter Options")
type_filter = st.sidebar.multiselect("Select Type:", df['type'].unique(), default=df['type'].unique())
country_filter = st.sidebar.multiselect("Select Country:", df['country'].dropna().unique()[:20])

# Filter dataset
filtered_df = df[(df['type'].isin(type_filter))]
if country_filter:
    filtered_df = filtered_df[filtered_df['country'].isin(country_filter)]

# Visualizations
st.subheader("🎬 Movies vs TV Shows")
type_count = filtered_df['type'].value_counts()
fig1, ax1 = plt.subplots()
ax1.bar(type_count.index, type_count.values)
st.pyplot(fig1)

st.subheader("📆 Content Added Over Years")
year_df = filtered_df['release_year'].value_counts().sort_index()
fig2, ax2 = plt.subplots()
ax2.plot(year_df.index, year_df.values, marker='o')
st.pyplot(fig2)

st.subheader("🌎 Top Countries with Most Content")
top_countries = filtered_df['country'].value_counts().head(10)
fig3, ax3 = plt.subplots()
ax3.barh(top_countries.index, top_countries.values)
st.pyplot(fig3)
