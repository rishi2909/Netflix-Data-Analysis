🎬 Project Description: Netflix Movies & TV Shows Analysis

This project explores the Netflix Titles Dataset using Data Analysis and Visualization techniques.
It consists of three key parts:

Dataset

Exploratory Data Analysis (Notebook)

Interactive Dashboard

📊 1. Dataset Description

Dataset Name: Netflix Movies and TV Shows Dataset (Kaggle)

Source: Kaggle
File: netflix_titles.csv
Total Entries: ~8,800 titles

📋 Columns Description
Column Name	Description
show_id	Unique ID for each show/movie
type	Whether it’s a Movie or TV Show
title	Title of the content
director	Director(s) of the content
cast	Main cast members
country	Country where the content was produced
date_added	Date the content was added to Netflix
release_year	Original release year
rating	TV rating (e.g., TV-MA, PG, R)
duration	Duration (minutes for movies or seasons for TV shows)
listed_in	Genre or category
description	Short summary of the content
🔍 Purpose:

The dataset helps analyze content trends, country contributions, rating distributions, and genre preferences on Netflix.

📓 2. Notebook (Exploratory Data Analysis)

The Jupyter Notebook performs the complete Data Cleaning, Exploration, and Visualization process.
It contains step-by-step insights such as:

🧹 Data Cleaning

Removed missing values and duplicates

Filled null entries with placeholders like "Unknown" or "Not Rated"

Converted date_added to datetime and extracted year_added

📈 Key Visualizations

Movies vs TV Shows Distribution

Content Added Over the Years

Top Countries Producing Netflix Content

Most Common Ratings

Genre Analysis (Word Cloud)

Trend of Content Release by Year

💡 Insights from Notebook

Netflix has more movies than TV shows.

Most content was released between 2015–2020.

The United States and India are top producers.

The most common rating is TV-MA, showing mature content dominates the library.

Popular genres include Dramas, Comedies, and Documentaries.

💻 3. Dashboard (Interactive Visualization)

The Streamlit Dashboard turns the EDA into an interactive app.
It allows users to explore the dataset in real time using filters and visualizations.

⚙️ Dashboard Features

Sidebar filters for Type, Country, and Rating

Interactive Plotly charts:

Bar chart: Movies vs TV Shows

Line chart: Content added by Year

Horizontal bar: Top Countries

Pie chart: Rating Distribution

Word Cloud: Genre popularity

Live table view of dataset preview

🎯 Purpose

To allow users to interactively explore Netflix content trends and gain insights through a visually appealing web interface.

🖼️ Dashboard Preview

(Add your screenshot here)

![Netflix Dashboard Screenshot](images/dashboard_preview.png)
