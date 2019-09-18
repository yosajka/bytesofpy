import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import statistics as st

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp/'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    input_file = csv.DictReader(open(MOVIE_DATA, newline='', encoding='utf-8'))
    res = defaultdict(list)
    for row in input_file:
        if row['title_year'] != '' and int(row['title_year']) >= MIN_YEAR:
            movie = Movie(row['movie_title'], int(row['title_year']), float(row['imdb_score']))
            res[row['director_name']].append(movie)
            if row['director_name'] in res.keys() and movie not in res[row['director_name']]:
                res[row['director_name']].append(movie)
    return res
res = get_movies_by_director()


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(st.mean([movie[2] for movie in movies]), 1)
    
a = calc_mean_score(res['Sergio Leone'])

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    scores = []   
    for key in directors.keys():
        if len(directors[key]) >= MIN_MOVIES:
            scores.append((key, round(st.mean([movie.score for movie in directors[key]]), 1)))
    scores = sorted(scores, key=lambda tup: tup[1], reverse=True)        
    return scores

test = get_average_scores(res)
print(test)