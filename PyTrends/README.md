# PyTrends
This is for PyTrends! NOT pytrend (that is a sadder unloved brother)

# https://pypi.org/project/pytrends/

# https://trends.google.com/trends/explore?cat=1392&geo=AT-9&q=Thailand,Seychellen,Maldiven

# https://trends.google.com/trends/explore?cat=1392&date=today%205-y&geo=AT-9&q=Thailand,Seychellen,Maldiven

# resources
https://www.premiumleads.com/en/blog/seo/how-to-get-google-trends-data-with-pytrends-and-python/

# notes
429 = google doesn't like you hitting their server so often

```The HTTP 429 Too Many Requests response status code indicates the user has sent too many requests in a given amount of time ("rate limiting"). A Retry-After header might be included to this response indicating how long to wait before making a new request.```


# use case one
Marketing question about product X in region Y speaks language Z.

You want to know how many times that X is mentioned is mentioned in regions A, B, C 


You want to know how many times that X is mentioned is mentioned in language F, G, H

Generate a graph showing this search trend.

# use case two
Your client, LittleCo, wants to know if their WidgetWonder is being searched in region A, B, C so they can retarget their ad campaigns.

Generate a graph showing this search trend.

# use case three
Your client, SuperCo, wants to know how often their industry, BasketWeaving, is being searched in languages F, G and H.

Generate a graph showing this search trend.

# use case four
Create a dashboard showing search trends over a time series by region.

# use case five
?

# use case six
Profit!!!

# URL for this repo
https://github.com/pleabargain/PyTrends

# target
https://www.google.com/alerts?hl=en-GB#

# categories or cat
* 67 = travel
* 179 = hotels and accomodations
* 1074 = beaches and islands
* 696 = luxury goods
* 1005 = ecotourism

# CZ
* cestovní kancelář = travel agency

# seychelles = %2Fm%2F06sw9
* https://trends.google.com/trends/explore?geo=CZ&q=%2Fm%2F06sw9


# inspired by
https://medium.com/@ismaelaraujo/pytrends-a-python-library-that-you-should-know-24764b384bc2

# why not just pass the request via the URL?
Google is obfuscating the request!
Check out what it does to my "sand dunes" query. It counts the number of chars but exposes nothing else.
![image](https://user-images.githubusercontent.com/640846/201508065-2838e0f0-c5e3-4b37-b40e-7b27a21affb0.png)


# graph
https://drive.google.com/file/d/13wUeT3ZHQvngwHiQMOKoPEb5WjIF8Fmm/view?usp=sharing

# TODO
* create stand alone functions and pass key words via the command line 
``` 

if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print ('Hello', name)

```

* get a list of all pn e.g. ```df = pytrend.trending_searches(pn='czech_republic')```
* fix graphs (still adding multiple search terms (kwlist) to same graph!)
* create a function that handles the graph generation
* pass arguments to the function
* * google_trends -filename.csv

* fix the output so that kwords is the search term
* search should use a csv for source e.g.
term, country(geo), language
chien,FR,FR
perro,ES,ES 
* * see https://pypi.org/project/pytrends/#interest-by-region
* use the sleep param in the module

```sleep

If you are rate-limited by Google, you should set this parameter to something (i.e. 60) to space off each API call.
```

# optional
* each search term graph has it's own PDF with a branded header and company logo
* * Not certain this is the way to go. 

# DONE
* added a logger
* added a minute time stamp to the files to make them easier to find!
* 60 second time between searches! 
* set a progress bar in terminal
* Set a timer in between running individual searches
## references
https://github.com/GeneralMills/pytrends/blob/master/examples/example.py


---

This is a fork.
## issues
I had to had some more pip install commands to get the script to run.

# errors
I got this one
`OSError: [WinError 5] Access is denied:`

I ran the pip install as admin cmd

