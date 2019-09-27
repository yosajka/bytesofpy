import requests
from collections import defaultdict
STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    cap = cap.strip('$')
    if 'M' in cap:
        cap = float(cap.strip('M'))
    elif 'B' in cap:     
        cap = float(cap.strip('B')) * 1000 
    return cap
            

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    summ = sum([_cap_str_to_mln_float(item['cap']) for item in data if item['industry'] == industry])
    return round(summ, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    highest_cap = 0
    for item in data:
        if _cap_str_to_mln_float(item['cap']) > highest_cap:
            highest_cap = _cap_str_to_mln_float(item['cap']) 
            symbol = item['symbol']
    return symbol
    

def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sector = {}  
    for item in data:
        if item['sector'] != 'n/a':
            if item['sector'] not in sector.keys():
                sector[item['sector']] = 0
            sector[item['sector']] += _cap_str_to_mln_float(item['cap'])
    res = [(k, v) for k, v in sector.items()]
    res = sorted(res, key=lambda x: x[1])
    return (res[-1][0], res[0][0])
        