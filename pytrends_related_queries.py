#install pytrends
# !pip install pytrends
#import the libraries
import date_time_helper_func as dthf
import pandas as pd
from pytrends.request import TrendReq
pytrends = TrendReq()

# keyword = "Maldives"
# keyword = "Seychelles"
keyword = "Thailand"
pytrends.build_payload(kw_list=[keyword])

related_queries = pytrends.related_queries()

# rising search returns what is popular now
df = pd.DataFrame(related_queries.get(keyword).get('rising'))

#top search seems to get everything ever for the keyword
#df = pd.DataFrame(related_queries.get(keyword).get('top'))

date_stamp = dthf.time_stamp_helper()

# create a function that saves the pandas dataframe to a csv
def save_to_csv(df, filename):
    df.to_csv(date_stamp, filename, index=False)
    print ("saved to csv")

print(list(df['query'][0:10]))
# TODO save the list to a file with a timestamp and the key word


