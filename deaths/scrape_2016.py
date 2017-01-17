import pandas as pd
from bs4 import BeautifulSoup
import requests
from calendar import month_name
import sys
r = requests.get('https://en.wikipedia.org/wiki/Deaths_in_January_2016')
print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')
days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = []
month = []
day = []
html = []
deaths = []
date_in_year = []
for mn in month_name:
    pass
for d in range(1, days_of_month[0] + 1):
    day_current = soup.find(class_='mw-headline', id=d)
    if day_current is None:
        # print(d, "Not exist")
        continue
    persons = day_current.parent.find_next_sibling('ul')
    #TODO: html.append(persons.prettify())
    html.append('X')
    day.append(d)
    month.append(1)
    year.append(2017)
    date_in_year.append('{:02d}{:02d}'.format(1, d))
    deaths.append(len(persons('li')))
data = {
    'date_in_year': date_in_year,
    'year': year,
    'month': month,
    'day': day,
    'deaths': deaths,
    'html': html
}
df = pd.DataFrame(data)
df['total_deaths'] = df.deaths.cumsum()
# df = df[['year','month','day','deaths','total_deaths','html']]
df = df[['date_in_year','deaths','total_deaths','html']]
df.to_csv('./2016.csv', index=False)
