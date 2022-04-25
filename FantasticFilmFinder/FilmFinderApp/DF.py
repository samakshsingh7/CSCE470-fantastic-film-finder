import pandas as pd
from decimal import Decimal
import os
from errno import EACCES
from pydoc import Doc
import math
import csv

csv_path = os.path.join(os.path.dirname(__file__), 'title_basics_data.tsv')
csv_path2 = os.path.join(os.path.dirname(__file__), 'title_rating_data.tsv')
csv_path3 = os.path.join(os.path.dirname(__file__), 'title_basics_rating.tsv')
basics_df = pd.read_csv(csv_path, sep='\t', dtype=str, nrows=10000)
basics_df['genres'] = basics_df['genres'].str.split(',')

rating_df = pd.read_csv(csv_path2, sep='\t', dtype=str, nrows=10000)

title_rating_df = pd.merge(left=basics_df, right=rating_df, left_on='tconst',right_on='tconst')

listGenres = set([])
for gen in title_rating_df['genres'].explode():
    listGenres.add(gen)
listGenres.discard('\\N')

hardcodedGenresSet = {'Sci-Fi', 'Romance', 'Mystery', 'Action', 'Western', 'History', 'News', 'Crime', 'Horror', 'Documentary', 'Adventure', 'Music', 'Comedy', 'Animation', 'Thriller', 'Family', 'Musical', 'Short', 'War', 'Sport', 'Fantasy', 'Biography', 'Drama'}
hardcodedGenres = ['Sci-Fi', 'Romance', 'Mystery', 'Action', 'Western', 'History', 'News', 'Crime', 'Horror', 'Documentary', 'Adventure', 'Music', 'Comedy', 'Animation', 'Thriller', 'Family', 'Musical', 'Short', 'War', 'Sport', 'Fantasy', 'Biography', 'Drama'].sort()

def listGenresDF():
    return hardcodedGenresSet
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


def get_each_title_freq(Documents):
    each_title_freq = {}
    for tconst in Documents:
        title = Documents[tconst]
        split_title = title.split()
        term_freq = {}
        for word in split_title:
            word = word.lower()
            if word in term_freq:
                term_freq[word] += 1
            else:
                term_freq[word] = 1
        for word in term_freq:
            term_freq[word] /= (len(split_title) + 2)
        each_title_freq[tconst] = term_freq
    return each_title_freq


def get_top_score_for_query(query):
    title_rating_df = pd.read_csv(csv_path3, sep='\t', dtype=str)
    Documents = title_rating_df.set_index('tconst').to_dict()['primaryTitle']

    tfs = get_each_title_freq(Documents)
    
    query = query.lower().split()
    query_tf = {}
    for word in query:
        if word in query_tf:
            query_tf[word] += 1
        else:
            query_tf[word] = 1
    for word in query_tf:
        query_tf[word] /= len(query)

    result_array = []
    for tconst in tfs:
        score = 0
        for word in query_tf:
            if word in tfs[tconst]:
                score += tfs[tconst][word] * query_tf[word]
        result = (score, tconst)
        result_array.append(result)

    result_array.sort(reverse=True)
    return_result = []
    # return_result = set()
    
    for i in range (0,15):
        tconst = result_array[i][1]
        return_result.append(title_rating_df.loc[title_rating_df.tconst == tconst, ['primaryTitle','startYear', 'endYear' , 'genres', 'averageRating']].values.flatten().tolist())
    return(return_result)

print(get_top_score_for_query("john wick"))


nums = [1,3]
num = {1:3}
def printer():
    prettyNums = ""
    for i in range(len(nums)):
        prettyNums += (str(nums[i])+"\n")
    return prettyNums
