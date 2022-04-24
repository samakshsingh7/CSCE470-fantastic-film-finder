import pandas as pd
from decimal import Decimal
import os

csv_path = os.path.join(os.path.dirname(__file__), 'title_basics_data.tsv')
csv_path2 = os.path.join(os.path.dirname(__file__), 'title_rating_data.tsv')
basics_df = pd.read_csv(csv_path, sep='\t', dtype=str, nrows=10000)
basics_df['genres'] = basics_df['genres'].str.split(',')

rating_df = pd.read_csv(csv_path2, sep='\t', dtype=str, nrows=10000)

title_rating_df = pd.merge(left=basics_df, right=rating_df, left_on='tconst',right_on='tconst')

listGenres = set([])
for gen in title_rating_df['genres'].explode():
    listGenres.add(gen)
listGenres.discard('\\N')

def listGenresDF():
    print(listGenres)

def genreListDF(user_genre):
    csv_path = os.path.join(os.path.dirname(__file__), 'title_basics_data.tsv')
    csv_path2 = os.path.join(os.path.dirname(__file__), 'title_rating_data.tsv')
    basics_df = pd.read_csv(csv_path, sep='\t', dtype=str, nrows=10000)
    basics_df['genres'] = basics_df['genres'].str.split(',')

    rating_df = pd.read_csv(csv_path2, sep='\t', dtype=str, nrows=10000)
    # movie_query = input("Input movie title: ")

    title_rating_df = pd.merge(left=basics_df, right=rating_df, left_on='tconst',right_on='tconst')
    if user_genre in listGenres:
        print("Top 10 movies in",user_genre,"genre")
        displayGenre = {}
        genre_df = title_rating_df[pd.DataFrame(title_rating_df.genres.tolist()).isin([user_genre]).any(1).values] #can handle multiple genres potentially
        return genre_df.sort_values('averageRating', ascending=False).head(10)
    else:
        print("Sorry, that genre is not in our database")


def searchDF(contains):
    movie_result = title_rating_df.loc[title_rating_df['primaryTitle'].str.contains(contains, case=False)]
    movie_result = movie_result.sort_values(by=['averageRating'], ascending=False)
    return movie_result



nums = [1,3]
num = {1:3}
def printer():
    prettyNums = ""
    for i in range(len(nums)):
        prettyNums += (str(nums[i])+"\n")
    return prettyNums