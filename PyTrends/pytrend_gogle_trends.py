# https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
#install pytrends
# !pip install pytrends
#import the libraries
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()
# Get Google Keyword Suggestions
keywords = pytrend.suggestions(keyword='Maldives')
df = pd.DataFrame(keywords)
df.head(5)