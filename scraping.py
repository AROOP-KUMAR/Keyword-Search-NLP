import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from summarize import summarizer


def web_scraper(query, results):
    ua = UserAgent()
    query = query.replace(' ', '+')
    URL = f'https://www.google.co.in/search?q={query}'
    headers = {'user-agent': ua.random}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        for g in soup.find_all('div', {'class': 'g'}):
            r = g.find('div', {'class': 'r'})
            if r:
                anchor = r.find('a')
                link = anchor['href']
                title = r.find('h3').text
            else:
                continue
            s = g.find('div', {'class': 's'})
            if s:
                header = s.find('span', {'class': 'st'}).text
            else:
                continue
            description = ""
            description = summarizer(link, headers)
            item = {
                'title': title,
                'link': link,
                'header': header,
                'description': description
            }
            results.append(item)
