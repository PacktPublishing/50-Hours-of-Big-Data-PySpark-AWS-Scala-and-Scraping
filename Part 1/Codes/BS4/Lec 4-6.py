from bs4 import BeautifulSoup
import requests
r = requests.get('https://quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
with open('bs4quotes.txt','w') as f:
    for tag in soup.findAll('span', {'class': 'text'}):
        f.write(tag.string)
        f.write('\n')