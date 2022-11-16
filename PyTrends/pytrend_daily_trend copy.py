#https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
# daily trends
#install pytrends
# !pip install pytrends
#import the libraries
import sys

import pandas as pd
from pytrends.request import TrendReq

def get_daily_trends():
    pytrend = TrendReq()
    #get today's treniding topics
    trendingtoday = pytrend.today_searches(pn='PL')
    return trendingtoday.head(20)
# pytrend = TrendReq()

# #get today's treniding topics
# trendingtoday = pytrend.today_searches(pn='PL')
# trendingtoday.head(20)

# #get today's treniding topics
# get_daily_trends()

if __name__ == "__main__":
    get_daily_trends(sys.argv)