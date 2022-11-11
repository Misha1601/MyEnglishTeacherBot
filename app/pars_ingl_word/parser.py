import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://english-verbs.ru/regular-verbs?page=1"
r = requests.get(URL_TEMPLATE)
# print(r.status_code)
# print(r.text)
soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('div', class_='entry-summary clearfix')
for name in vacancies_names:
    a = name.p.contents
    print(a[1].get_text(strip=True))
    print(str(a[2].get_text(strip=True)).split(',')[0])
    print(a[3].get_text(strip=True))
    break