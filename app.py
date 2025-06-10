import streamlit as st
import pandas as pd
from recommend import recommend_movie

# Load data
try:
    movie_matrix = pd.read_csv("movie_matrix.csv", index_col=0)
    movies = list(movie_matrix.columns)
except FileNotFoundError:
    st.error("movie_matrix.csv not found. Please run preprocess.py first.")
    movies = []

# Page setup
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Sidebar
st.sidebar.title("🎬 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Recommend", "About"])

# Home page
if page == "Home":
    st.title("📽️ Movie Recommender System")
    st.markdown("""
    Welcome to the Movie Recommender App!  
    This app helps you discover movies similar to the one you love, using **KNN and cosine similarity**.
    """)
    st.image("images\cinema.jpg", use_container_width=True)


# Recommendation page
elif page == "Recommend":
    st.title("🔍 Find Similar Movies")

    if movies:
        selected_movie = st.selectbox("🎞️ Select a movie you like", movies, key="movie_selector")

        if st.button("Get Recommendations"):
            recs = recommend_movie(selected_movie)
            if isinstance(recs, str):
                st.error(recs)
            else:
                st.success("🎯 Recommended Movies:")
                for movie in recs:
                    st.write("🎥", movie)
    else:
        st.warning("Movie list not available. Please check your dataset.")

# About page
elif page == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
    - **Dataset:** MovieLens 100K  
    - **Algorithm:** K-Nearest Neighbors (KNN) with Cosine Similarity  
    - **Libraries Used:** pandas, scikit-learn, Streamlit  
    - **Purpose:** Recommend movies based on user rating patterns  
    - **Built By:** [Your Name]
    """)
    st.markdown("Made with ❤️ using Streamlit.")
