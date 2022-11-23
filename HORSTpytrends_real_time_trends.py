# Path: HORSTpytrends_real_time_trends.py

#real time trends in a country
#install pytrends
# !pip install pytrends
#import the libraries
import sys
import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()
# Get realtime Google Trends data
# df = pytrend.trending_searches(pn='united_states')
df = pytrend.trending_searches(pn='czech_republic')

print(df.head())
#TODO save results to csv with timestamp and search term
# TODO pass search term to the function
# TODO create a list of search terms that user can select from and pass it to the function
# TODO create a list of countries that user can select from and pass it to the function

