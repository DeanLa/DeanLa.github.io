import pandas as pd
from bs4 import BeautifulSoup
import requests
from calendar import month_name

r = requests.get('https://en.wikipedia.org/wiki/Deaths_in_2017#January')
print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')

html = []
deaths = []
date_in_year = []
month_dict = {}
for i,month in enumerate(month_name):
    month_dict[month] = "{:02d}".format(i)

# Scrape
mw_headlines = soup.find_all(class_='mw-headline')
for d in mw_headlines:
    try:
        if d.string in month_dict.keys():
            print (d)
            mi = month_dict[d.string]
        else:
            di = "{:02d}".format(int(d.string))
            persons = d.parent.find_next_sibling()
            if persons.name != 'ul':
                continue
            html.append('X')
            date_in_year.append(mi+di)
            deaths.append(len(persons('li')))

    except Exception as e:
        print (e)
data = {
    'date_in_year': date_in_year,
    'deaths': deaths,
    'html': html
}
df = pd.DataFrame(data)
df = df.sort_values(by='date_in_year', ascending=True)
df['total_deaths'] = df.deaths.cumsum()
df.to_csv('./2017.csv', index=False)


import os
import datetime
print (os.getcwd())

os.system('git add 2017.csv')
os.system('git commit -m "Data {}"'.format(datetime.datetime.now()))
os.system('git push origin master')
