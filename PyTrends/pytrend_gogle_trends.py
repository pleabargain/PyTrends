# https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
#install pytrends
# !pip install pytrends
#import the libraries
import date_time_helper_func
import time
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()
# Get Google Keyword Suggestions
# kw = "Maldives"
# read the searchlst
# iterate over the lst 
# feed the iteration to the script

def search_keywords(keyword_list):
    for kw in keyword_list:
        print('processing', kw)
        keywords = pytrend.suggestions(keyword=kw)
        df = pd.DataFrame(keywords)
        print(df.head(10))
        df.to_csv( 'output/data/'+ date_time_helper_func.time_stamp_helper() + '_' + kw + '.csv', index=False)
        time.sleep (1)
    print("Done")

def search_keyword_from_search_list(filename):
    keyword_list =[]
    with open('searchlist.txt', 'r') as f:
        for line in f:
            keyword_list.append(line.strip())
    print("done reading the file")
    search_keywords(keyword_list)

search_keyword_from_search_list('searchlst.txt')

# keyword_list =[]
# with open('searchlst.txt', 'r') as f:
#     for line in f:
#         keyword_list.append(line.strip())
# print('processing, keywordlist...')
# search_keywords(keyword_list)


#trendingtoday = pytrend.today_searches(pn='PL')
# create a csv with the data 
def search_country_trends(country_code_list_file="countrylist.txt"):
    
    country_code_list =[]
    with open(country_code_list_file, 'r') as f:
        for line in f:
            country_code_list.append(line.strip())
    print("done reading the file")
    for country_code in country_code_list:
        
        print('processing', country_code)
        df = pytrend.today_searches(pn=country_code)
        print(df.head(10))
        df.to_csv( 'output/data/'+ date_time_helper_func.time_stamp_helper() + '_' + country_code + '.csv', index=False)
        time.sleep(1)

search_country_trends()