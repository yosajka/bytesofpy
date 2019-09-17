import glob
import json
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movie_data = []
    for movie in files:
        with open(movie, 'r') as f:
            a = json.load(f)
            movie_data.append(a)
    return movie_data

movies = get_movie_data(files=files)
#print([a['Title'] for a in movies])

def get_single_comedy(movies):
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']
        

def get_movie_most_nominations(movies):
    nominations = []
    for movie in movies:
        nominations.append(sum([int(s) for s in movie['Awards'].split() if s.isdigit()]))
    for movie in movies:
        if sum([int(s) for s in movie['Awards'].split() if s.isdigit()]) == max(nominations):
            return movie['Title']


def get_movie_longest_runtime(movies):
    run_time = []
    movie_name = []
    for movie in movies:
        length = sum([int(s) for s in movie['Runtime'].split() if s.isdigit()])
        run_time.append(length)
    for movie in movies:
        if sum([int(s) for s in movie['Runtime'].split() if s.isdigit()]) == max(run_time):
            return movie['Title']
    