#https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
# daily trends
#install pytrends
# !pip install pytrends
#import the libraries
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()

#get today's trending topics
# Get Google Top Charts
# only works on historical data
df = pytrend.top_charts(2021, hl='en-US', tz=300, geo='GLOBAL')
df.head()
# trendingtoday = pytrend.today_searches(pn='PL')
# trendingtoday.head(20)A