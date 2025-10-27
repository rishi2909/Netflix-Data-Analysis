📊 Dataset Description

Source: Netflix Movies and TV Shows (Kaggle)

Rows: 8,807

Columns: 12

Features:

type → Movie or TV Show

title → Name of the content

director → Director(s) of the content

cast → Main actors/actresses

country → Country of origin

release_year → Year of release

rating → Age rating (e.g., TV-MA, PG-13)

duration → Duration in minutes or number of seasons

listed_in → Genres or categories

description → Short summary

📒 Notebook Analysis

The Jupyter Notebook (netflix-dataset-analysis-updated.ipynb) covers:

Data Cleaning & Preprocessing

Exploratory Data Analysis (EDA)

Insights on:

Most popular genres

Content distribution across countries

Release year trends

Rating distributions

Visualizations using Matplotlib, Seaborn, and WordCloud

Example visualization:


💻 Interactive Dashboard

The Streamlit Dashboard (app.py) allows users to:

Filter by Type and Country

Explore Movies vs. TV Shows

View Content Trends Over the Years

Analyze Top Countries

See Ratings Distribution

Dashboard preview:


🚀 Technologies Used

Python 🐍

Pandas – Data cleaning and manipulation

Matplotlib & Seaborn – Data visualization

Plotly – Interactive visualizations

Streamlit – Dashboard development

⚙️ How to Run the Dashboard

Install dependencies

pip install pandas matplotlib seaborn plotly streamlit


Run the Streamlit app

streamlit run app.py


Open in Browser

http://localhost:8501

💡 Insights

The majority of Netflix content is Movies, not TV Shows.

United States and India are top producers of Netflix content.

A significant spike in new releases was observed after 2015.

The most common rating category is TV-MA (Mature Audience).

The Drama and Comedy genres dominate Netflix’s library.

📸 Dashboard Gallery
Dashboard Section	Preview
Home	

Filter Section	

Charts	
✨ Future Enhancements

Add genre-based filtering

Include recommendation engine

Deploy on Streamlit Cloud for live demo

👨‍💻 Author

Rishi Raj
📧 [Your Email or LinkedIn]
🌐 GitHub Profile Link
