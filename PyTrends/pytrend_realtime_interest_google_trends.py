# Import pandas and pytrends using below lines
import pandas as pd
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=91, timeout=(10,25),retries=2, backoff_factor=0.1, requests_args={'verify':False})

geo = 'CZ' 
keyword_list = ['Twitter', 'Elon Musk']
time_interval = 'now 7-d'
pytrends.build_payload(keyword_list, cat=0, timeframe=time_interval, geo=geo)

df = pytrends.interest_over_time()
print(f"total records fetched for   {geo}" ,df.size)
df.head()