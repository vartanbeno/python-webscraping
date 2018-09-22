from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())