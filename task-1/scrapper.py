import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.worldometers.info/coronavirus/')
countrys=[] 
cases=[] 
deaths=[] 
recovereds =[]
soup = BeautifulSoup(r.content, 'html.parser')
body = soup.find('tbody')
body.prettify()
# print(body.text)
for a in body.findAll('tr'):
    tds = a.find_all('td')
    if (tds[1].find('a')) is None:
        continue
    if(int(tds[0].text)<11):
        country=tds[1].find('a').text
        case=tds[2].text
        death= tds[4].text.strip()
        recovered = tds[6].text
        countrys.append(country)
        cases.append(case)
        deaths.append(death)
        recovereds.append(recovered)
print("done, check the data.csv file in task-1 folder")

df = pd.DataFrame({'Country':countrys,'total cases':cases,'total Death':deaths,'total Recovered':recovereds}) 
df.to_csv('task-1\\data.csv', index=False, encoding='utf-8')

"""
Though line 13 & 14 have error squiggles under them ,
they are working completely fine, just ignore them.
"""