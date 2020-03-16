from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import re
import pandas as pd


def read_file():
    file = open('coding bat java html.txt')
    data = file.read()
    file.close()
    return data

data = {'Topic': [] , 'Question': [], 'Description':[] }
t=[]
q=[]
d=[]
soup = BeautifulSoup(read_file(), 'html.parser')
ua = UserAgent()
all_divs = soup.find_all('div', attrs={'class': 'summ'})
products = {div.a.span.string: div.a['href'] for div in all_divs}
for key, value in products.items():
    url = "https://codingbat.com" + value
    #print(key, "\n")
    t.append(key)
    page1 = requests.get(url, headers={'user-agent': ua.chrome})
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    for link in soup1.find_all("a", href=re.compile("prob")):
        #print(link.string)
        q.append(link.string)
        url1 = "https://codingbat.com" + link.get('href')
        page2 = requests.get(url1, headers={'user-agent': ua.chrome})
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        for divs in soup2.find_all('div', attrs={'class': 'minh'}):
            d.append(divs.p.text)
            t.append(" ")
            t.append(" ")
            for sibling in divs.next_siblings:
                if sibling.string is not None:
                    d.append(sibling)
                    q.append(" ")
                    t.append(" ")





#dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in mydict.items() })

data.update({'Topic': t, 'Question': q, 'Description': d})
df = pd.DataFrame({key: pd.Series(value) for key, value in cars.items()})
export_csv = df.to_csv (r'D:\PYTHON LEARNING LECTURES CODES\SECOND LECTURE CODES\webscraping_data.csv', index = None, header=True)

