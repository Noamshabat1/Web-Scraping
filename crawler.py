import bs4
import requests
import sys


def prints_the_html_sources(html):
    response = requests.get(html)
    html = response.text
    soup = bs4.BeautifulSoup(html)
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        links = p.find_all("a")
        for l in links:
            l.get('href')
            print(base_link_url + l['href'])


base_link_url = "https://en.wikipedia.org"

if __name__ == '__main__':
    prints_the_html_sources(sys.argv[1])
