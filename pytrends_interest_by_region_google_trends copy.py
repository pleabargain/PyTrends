# Import pandas and pytrends using below lines
import pandas as pd
import pytrends
from pytrends.request import TrendReq

# pytrends = TrendReq(hl='en-US', tz=91, timeout=(10,25),retries=2, backoff_factor=0.1, requests_args={'verify':False})

geo = 'CZ'
# search in Czech Republic for travel to Maldives
# keyword_list = ['cestování po Maledivách', 'Gili']

# keyword_list = ['cestování po Maledivách', ]

keyword_list = ['cestování', "Dubai" ]
# convert to string
var_keyword_list = [str(item) for item in keyword_list]

# time_interval = 'now 7-d'
pytrends.build_payload(keyword_list, cat=0, timeframe=time_interval, geo=geo)

# df = pytrends.interest_over_time()
# print(f"total records fetched for   {geo}" ,df.size)
# df.head()

pytrends.interest_by_region(resolution='COUNTRY', 
                            inc_low_vol=True, 
                            inc_geo_code=False)

df = pytrends.interest_by_region()
print(f"{var_keyword_list} 'travel' interest by region: {df.size}")
print(df.head())