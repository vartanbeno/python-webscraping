from bs4 import BeautifulSoup
import requests


with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


'''
Parse the whole file.
'''
# print(soup.prettify())


'''
Parse title tag.
'''
match = soup.title
print(match)
print(match.text)


'''
Search for div with class "footer".
'''
match = soup.find('div', class_='footer')
print(match)
