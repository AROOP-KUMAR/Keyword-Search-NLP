from gensim.summarization.summarizer import summarize
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_only_text(url, headers):
    req = Request(url, headers=headers)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return text


def summarizer(url, headers):
    text = get_only_text(url, headers)
    try:
        summary = summarize(str(text), word_count=100)
        if summary:
            return summary
        else:
            return "No description available"
    except Exception as e:
        return "No description available"
