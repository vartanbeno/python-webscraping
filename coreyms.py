from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

articles = soup.find_all('article')
for article in articles:
    header = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    try:
        video_src = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
    except Exception as e:
        video_src = None
    print(header)
    print(summary)
    print(f'https://www.youtube.com/watch?v={video_src}')
    print()

