#https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
# daily trends
#install pytrends
# !pip install pytrends
#import the libraries
import pandas as pd
from pytrends.request import TrendReq
pytrends = TrendReq()

# build the payload
pytrends.build_payload(kw_list=['Maldives'], timeframe='2020-01-01 2022-11-01', geo='CZ') 

# get related topics
df_rt = pytrends.related_topics()
# print (df_rt)
# display top 5 rising results for the chicken keyword
print(df_rt['Maldives']['rising'].head(5))