import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load user-movie rating matrix
movie_matrix = pd.read_csv("movie_matrix.csv", index_col=0)

# Transpose to get movie-wise vectors
movie_features = movie_matrix.T

# Fit KNN model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(movie_features)

movie_titles = list(movie_features.index)

def recommend_movie(movie_name, top_n=5):
    if movie_name not in movie_titles:
        return "Movie not found in database"

    movie_index = movie_titles.index(movie_name)
    movie_vector = movie_features.iloc[movie_index].values.reshape(1, -1)
    
    distances, indices = model.kneighbors(movie_vector, n_neighbors=top_n+1)  # +1 to skip itself

    recommendations = []
    for idx in indices.flatten()[1:]:  # Skip the input movie itself
        recommendations.append(movie_titles[idx])

    return recommendations

# Test
if __name__ == "__main__":
    print("Recommendations for Toy Story (1995):")
    print(recommend_movie("Toy Story (1995)"))
