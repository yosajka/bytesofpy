import os
import urllib.request

LOG = os.path.join('/tmp/', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    with open(LOG, 'r') as logfile:
        content = logfile.read().split('\n')   
    date = list(set([text[:5] for text in content if text[:5] != '']))
    date = sorted(date, key=lambda x: int(x[3:5]))    
    for days in date:
        pybook = ''
        for i in range(1, len(content), 2):
            if 'slack' in content[i] and days in content[i]:
                if 'python' in content[i-1].lower():
                    pybook = pybook + '🐍'
                else:
                    pybook = pybook + '.'
        if pybook != '':
            print(days + ' ', end='')            
            print(pybook)
                        
create_chart()            