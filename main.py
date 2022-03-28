import pandas as pd
from decimal import Decimal


basics_df = pd.read_csv('title_basics_data.tsv', sep='\t', dtype=str, nrows=10000)
basics_df['genres'] = basics_df['genres'].str.split(',')

rating_df = pd.read_csv('title_rating_data.tsv', sep='\t', dtype=str, nrows=10000)
movie_query = "John"

title_rating_df = pd.merge(left=basics_df, right=rating_df, left_on='tconst',right_on='tconst')

movie_result = title_rating_df.loc[title_rating_df['primaryTitle'].str.contains(movie_query, case=False)]
movie_result = movie_result.sort_values(by=['averageRating'], ascending=False)

print(movie_result)

# We are currently testing our searching to not only find name including the query word but also related to the query word
# Such as Jon, Jonny, Johny, Jojo, ... and insert that into the name searching
