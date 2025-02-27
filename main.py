import matplotlib as plt
import seaborn as sns
import pandas as pd

movies = pd.read_csv("csv/movie_rating.csv")

print(movies)

m1 = sns.displot(movies.AudienceRatings, bin =10)