import pandas as pd
import matplotlib.pyplot as plt

# df = pd.DataFrame([[2001,151],[2002,160], [2006,211]], columns=['year','sale'])
# print (df)
# df.to_csv('./data.csv', index=False)
# {'split','records','index','columns','values'}
# plt.plot (df.x, df.y)
# plt.show()

from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/Deaths_in_2017#January')
print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')
days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = {"January"}

year = []
month = []
day = []
html = []
deaths = []
date_in_year = []

for d in range(1, days_of_month[0] + 1):
    day_current = soup.find(class_='mw-headline', id=d)
    if day_current is None:
        continue
    persons = day_current.parent.find_next_sibling()
    if persons.name != 'ul':
        continue
    # print (persons.name)
    # print ('\n\n\n')
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
df.to_csv('./2017.csv', index=False)

import os
import datetime
print (os.getcwd())

# os.system('git add 2017.csv')
# os.system('git commit -m "Data {}"'.format(datetime.datetime.now()))
# os.system('git push origin master')
