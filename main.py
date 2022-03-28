import pandas as pd 
pd.options.display.width = 0


name_basics_df = pd.read_csv('title_basics_data.tsv', sep='\t', dtype=str, nrows=5000)
title_basics_df = pd.read_csv('title_rating_data.tsv', sep='\t', dtype=str, nrows=5000)



# title = title_akas_df[title_akas_df["region"]=="US"]
# title_basics_df = title_basics_df[title_basics_df["startYear"] > 2000]


print(name_basics_df)

title_merged = pd.merge(left=name_basics_df, right=title_basics_df, left_on='tconst',right_on='tconst')
# title_merged = title_merged[title_merged['titleType']=="movie"]
# title_merged = pd.merge(left=title_merged, right = title_rating_df, left_on='titleId', right_on='tconst')
# title_merged = pd.merge(left=title_merged, right = title_crew_df, left_on='titleId', right_on='tconst1')
# title_merged=title_merged.drop(labels=['numVotes','tconst','tconst1','ordering','language','types','attributes','isOriginalTitle','titleType','primaryTitle','originalTitle','isAdult','endYear'],axis=1)

#Converts title_merged df into dictionary (Format --> {movieName : {'titleId' : ..., 'Year': ..., etc.)
title_dict = {title_merged['primaryTitle'][index]:{} for index in title_merged.index}

for index in title_merged.index:
    movieName = title_merged['primaryTitle'][index]
    title_dict[movieName] = {'primaryTitle' : title_merged['primaryTitle'][index],'Year' : title_merged['startYear'][index],'Runtime' : title_merged['runtimeMinutes'][index], 'Rating' : title_merged['averageRating'][index], 'Genre' : title_merged['genres'][index]}


count = 0
for i in title_dict:
    count += 1
    if count < 10:
        print(i, title_dict[i])
