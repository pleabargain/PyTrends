# PyTrends

# target
https://www.google.com/alerts?hl=en-GB#

# inspired by
https://medium.com/@ismaelaraujo/pytrends-a-python-library-that-you-should-know-24764b384bc2

# why not just pass the request via the URL?
Google is obfuscating the request!
Check out what it does to my "sand dunes" query. It counts the number of chars but exposes nothing else.
![image](https://user-images.githubusercontent.com/640846/201508065-2838e0f0-c5e3-4b37-b40e-7b27a21affb0.png)


# URL for this repo
https://github.com/pleabargain/PyTrends

# graph
https://drive.google.com/file/d/13wUeT3ZHQvngwHiQMOKoPEb5WjIF8Fmm/view?usp=sharing

# TODO
* pass arguments to the function
* * key word (kw) csv
* search should use a csv for source e.g.
term, country(geo), language
chien,FR,FR
perro,ES,ES 
* * see https://pypi.org/project/pytrends/#interest-by-region
* each search term graph has it's own PDF with a branded header and company logo

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

