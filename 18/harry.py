import os
import urllib.request
from collections import Counter
import re
# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    stopword = open(stopwords_file, 'r')
    list_sw = stopword.read().split("\n")
    harry = open(harry_text, 'r')
    content_harry = harry.read().lower()
    content_harry = re.sub("[^A-Z'a-z0-9]+", ' ', content_harry).lstrip()    
    list_harry = content_harry.split()
    for word in list_sw:
        list_harry[:] = [value for value in list_harry if value != word]
    return Counter(list_harry).most_common(1)[0]