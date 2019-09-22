from collections import Counter, defaultdict
import csv
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')

content = get_season_csv_file(1)


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    content = list(csv.reader(content.splitlines(), delimiter=','))
    characters = [name[2] for name in content]
    characters = list(dict.fromkeys(characters))
    del characters[0]
    res = defaultdict()
    for character in characters:
       episode = 1
       dic = {}
       count = 0
       for row in content: 
          if row[2] == character:
            if str(episode) == row[1]:
               count += len(row[3].split())
            else:
               dic[str(episode)] = count
               episode = int(row[1])
               count = len(row[3].split())
       if '13' not in dic.keys():
          dic['13'] = count 
       dic = Counter(dic)
       res[character] = dic
    return res
      
'''Revised solution'''
# def get_num_words_spoken_by_character_per_episode(content):
#    reader = csv.DictReader(content.splitlines(), delimiter=',')
#    words_spoken = defaultdict(lambda: Counter())
#    for row in reader:
#       episode = row['Episode']
#       line = row['Line']
#       words_spoken[row['Character']][episode] += len(line.split())
#    return words_spoken   

   


                
          



    
