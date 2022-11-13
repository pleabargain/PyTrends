

## install  the libs
# !pip install pytrends
# !pip install statsmodels user
# !pip install seaborn

from time import sleep
import logging

from tqdm import tqdm
# note: tqdm is a progress bar library
# note need to give pytrends a break, otherwise it will get blocked 
# TODO set the time between as a user input
for _ in tqdm(range(1)):
    sleep(1)

# %%
import pytrends
from pytrends.request import TrendReq
import pandas as pd
# from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import numpy as np
import datetime as dt

from datetime import datetime
# from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
# time the script run time
import time
# set variable for start time of the script

startTime = time.time()
currentDateAndTime = datetime.now()




# Create and configure logger
logging.basicConfig(filename="PyTrends/PytrendPerformance.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG produces a LOT of information
# https://docs.python.org/3/howto/logging.html
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)



# Notebook settings
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', None)
# TODO figuure out how to override the defaults here
pytrends = TrendReq(hl='en_US', tz=360)

# open csv file with the keywords
read_csv_file = pd.read_csv(r'C:/Users/denni/OneDrive/Documents/PyTrends/PyTrends/search_terms.csv')
# loop through the csv file and get the first row of data
for i in range(len(read_csv_file)):
    print(read_csv_file.loc[i, "search_terms"])

#TODO pass the search terms to the kw_list variable
kw_list = ["search_terms"]

# TODO I can't change this value! If I do I get an error!
# kw_list = ['Intercontinental Phuket']

frequency = 'daily' # must be  hourly or daily
# for whatever reason, I can't get a different Geo to work e.g. CZ
geo = 'US'
hl='en_US'

# Select Start Date
year_start = 2022
month_start = 1
day_start=1
hour_start=0

# Select End Date
year_end=2022
month_end=12
day_end=31
hour_end=0

# Run PyTrends
google_trends = pytrends.get_historical_interest(kw_list,
                                 year_start = year_start, 
                                 month_start = month_start, 
                                 day_start = day_start, 
                                 hour_start = hour_start, 
                                 year_end = year_end, 
                                 month_end = month_end, 
                                 day_end = day_end, 
                                 hour_end = hour_end, 
                                 cat=0, 
                                 geo=geo, 
                                 gprop='', 
                                 sleep=0,
                                 frequency=frequency)


google_trends = google_trends.reset_index()
google_trends.columns = ['date', 'keyword','partial']
google_trends.drop(['partial'], axis=1, inplace=True)
pd.to_datetime(google_trends['date'])
# show the top 5 rows (sanity check)
google_trends.head()

# set day variable
today =  datetime.now()
# create a date object
d1 = today.strftime("%M__%Y-%m-%d %H:%M")

# seaborn graph settings
sns.set(rc={"figure.figsize":(14, 6)})
sns.lineplot(data=google_trends, x='date', y='keyword')

plt.xlabel('Date', fontsize = 18)
plt.ylabel(str(kw_list), fontsize = 18)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
# save the graph to the file system
plt.savefig('PyTrends/output/images/'+str(kw_list) +'_' +'_' + d1 +'_'+ "google_trend_plot.png", dpi=360, bbox_inches='tight')
# notify the user that the graph has been saved
print('Graph saved to the file system')
# log the graph save
logger.info('Graph saved to the file system')
# uncomment to show the plot
# plt.show()




# write search results to csv
google_trends.to_csv((kw_list[0]) + '_'+ d1+'.csv')


# print user script is complete
print('User script is complete')

# print location of the files
print('Google Trends file saved to: ' + str(kw_list[0]) + '_'+ d1+'.csv')
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

google_trends
