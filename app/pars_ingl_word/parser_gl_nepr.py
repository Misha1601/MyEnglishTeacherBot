import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

URL_TEMPLATE = "https://english-verbs.ru/irregular-verbs?page="
# print(r.status_code)
# print(r.text)
gl = {}
for i in range(1,12):
    urls = f"{URL_TEMPLATE}{i}"
    r = requests.get(urls)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('div', class_='entry-summary clearfix')
    for name in vacancies_names:
        a = name.p.contents
        c = a[1].get_text(strip=True)
        d = str(a[2].get_text(strip=True)).split(',')[0][1:-1]
        e = a[3].get_text(strip=True)
        f = str(a[8].get_text(strip=True))

        g = f[f.find('(')+1:f.find(')')]
        f = f[f.find(')')+1:]
        # print(f)
        h = f[f.find('(')+1:f.find(')')]
        f = f[f.find(')')+1:]
        k = f[f.find('(')+1:f.find(')')]

        gl[c] = [d, e, [g, h, k]]

        # print(c, d, e, [g, h, k])
        # break
    # break
# print(gl)
# print(len(gl))
# with open('word_gl_nepr.json', 'w') as file:
#     json.dump(gl, file, ensure_ascii=False, indent=4)

# with open('word_gl_nepr.json') as file:
#     tr =json.load(file)
# print(len(tr))
# print(tr)