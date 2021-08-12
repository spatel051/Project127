import requests
import pandas as pd
from bs4 import BeautifulSoup

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

star_names = []
distance = []
mass = []
radius = []

page = requests.get(start_url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
table_rows = table.find_all('tr')

temp_list = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    
df = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns = ['Star Name', 'Distance', 'Mass', 'Radius'])
df.to_csv('Project127.csv')