import pandas as pd

movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')

print("Movies:\n",movies.head())
print("\nRatings:\n",ratings.head())
