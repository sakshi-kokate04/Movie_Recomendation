import pandas as pd

# Load data
movies = pd.read_csv("ml-latest-small/movies.csv")
ratings = pd.read_csv("ml-latest-small/ratings.csv")

# Merge data on movieId
data = pd.merge(ratings, movies, on='movieId')

# Create a pivot table for collaborative filtering
movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN with 0 (or use other imputation methods)
movie_matrix.fillna(0, inplace=True)

# Save for later use
movie_matrix.to_csv("movie_matrix.csv")
print("Matrix saved.")
