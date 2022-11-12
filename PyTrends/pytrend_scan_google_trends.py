# %% [markdown]
# ### Google Trends

# %% [markdown]
# #### 1. Install PyTrends

# %%
## install  the libs
# !pip install pytrends
# !pip install statsmodels user
# !pip install seaborn



# %%
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import numpy as np
import datetime as dt
from datetime import date
from pytrends.request import TrendReq
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
import matplotlib.pyplot as plt

import warnings

# Notebook settings
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', None)
pytrends = TrendReq(hl='en_US', tz=360)
# sns.set_theme()

# %% [markdown]
# #### Retrieve Google Trends Data

# %%
# kw_list = ['Pimalai Resort & Spa']

kw_list = ['Intercontinental Phuket']
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
month_end=11
day_end=19
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

# %%
# Plot google trends over time
today = date.today()
# create a date object
d1 = today.strftime("%Y_%m_%d")

sns.set(rc={"figure.figsize":(14, 6)})

sns.lineplot(data=google_trends, x='date', y='keyword')
plt.xlabel('Date', fontsize = 18)
plt.ylabel(str(kw_list), fontsize = 18)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.savefig(str(kw_list) +'_' +'_' + d1 +'_'+ "google_trend_plot.png", dpi=360, bbox_inches='tight')
plt.show()

# %%
# Plot google trends over time
# sns.set(rc={"figure.figsize":(14, 4)})

# sns.lineplot(data=google_trends, x='date', y='keyword')
# plt.xlabel('Date')
# plt.ylabel(str(kw_list))
# # plt.savefig("google_trend_plot.jpg", dpi=360, bbox_inches='tight')
# plt.show()

# %%
# Save Google Trends file
today = date.today()
# create a date object
d1 = today.strftime("%Y_%m_%d")
# google_trends.to_csv('google_trends_'+ kw_list[0]+'_'+ d1+'.csv')
google_trends.to_csv((kw_list[0]) + '_'+ d1+'.csv')

# %% [markdown]
# ### Google Trends Keywords Suggestion

# %%
# Get Google Keyword Suggestions
# pytrend = TrendReq()
# # it's not going to take any other language as EN is hardcoded
# keywords = pytrend.suggestions(keyword='Pimalai Resort & Spa')
# df = pd.DataFrame(keywords)
# df.head(10)

# # %% [markdown]
# # ### Dummy Variables

# # %% [markdown]
# # #### Federal Holidays

# # %%
# google_trends
# google_trends.head()

# # %%
# cal = calendar()
# holidays = cal.holidays(start = google_trends['date'].min(), end = google_trends['date'].max())
# google_trends['holiday'] = google_trends['date'].isin(holidays)
# google_trends['holiday'] = google_trends['holiday'].apply(lambda x: 1 if x == True else 0)
# google_trends.head()

# # %% [markdown]
# # #### Day of the Week

# # %%
# # Getting the day of the week
# google_trends['d'] = google_trends['date'].dt.dayofweek

# # Creating is_weekday variable
# google_trends['is_weekday'] = google_trends['d'].apply(lambda x: 1 if x != 5 and x !=6 else 0)

# # Creating is_weekend variable
# google_trends['is_weekend'] = google_trends['d'].apply(lambda x: 1 if x == 5 or x == 6 else 0)
# google_trends.head()

# # %%
# google_trends['d'] = google_trends['d'].apply(lambda x: 'Monday' if x == 0 else
#                               'Tuesday' if x == 1 else
#                               'wednesday' if x == 2 else
#                               'thursday' if x == 3 else
#                               'friday' if x == 4 else
#                               'saturday' if x == 5 else
#                               'sunday' if x == 6
#                     else x)

# # %%
google_trends


