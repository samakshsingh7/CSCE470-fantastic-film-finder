import pandas as pd
from decimal import Decimal


basics_df = pd.read_csv('title_basics_data.tsv', sep='\t', dtype=str, nrows=10000)
basics_df['genres'] = basics_df['genres'].str.split(',')

rating_df = pd.read_csv('title_rating_data.tsv', sep='\t', dtype=str, nrows=10000)
movie_query = input("Input movie title: ")

title_rating_df = pd.merge(left=basics_df, right=rating_df, left_on='tconst',right_on='tconst')

movie_result = title_rating_df.loc[title_rating_df['primaryTitle'].str.contains(movie_query, case=False)]
movie_result = movie_result.sort_values(by=['averageRating'], ascending=False)

print("Movies results for the query '" + movie_query + "'")
print(movie_result)

listGenres = set([])
for gen in title_rating_df['genres'].explode():
    listGenres.add(gen)

listGenres.discard('\\N')
print("\n")
print(listGenres)

print("To see movies based on genre, type a genre from the above list")
user_genre = input()
print("\n")
if user_genre in listGenres:
    print("Top 10 movies in",user_genre,"genre")
    displayGenre = {}
    genre_df = title_rating_df[pd.DataFrame(title_rating_df.genres.tolist()).isin([user_genre]).any(1).values] #can handle multiple genres potentially
    print(genre_df.sort_values('averageRating', ascending=False).head(10))
else:
    print("Sorry, that genre is not in our database")

# We are currently testing our searching to not only find name including the query word but also related to the query word
# Such as Jon, Jonny, Johny, Jojo, ... and insert that into the name searching
