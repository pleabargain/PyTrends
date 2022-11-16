#real time trends
#install pytrends
# !pip install pytrends
#import the libraries
import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()
# Get realtime Google Trends data
# df = pytrend.trending_searches(pn='united_states')
df = pytrend.trending_searches(pn='czech_republic')

df.head()