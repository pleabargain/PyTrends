#https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
# daily trends
#install pytrends
# !pip install pytrends
#import the libraries
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()

#get today's treniding topics
trendingtoday = pytrend.today_searches(pn='PL')
trendingtoday.head(20)