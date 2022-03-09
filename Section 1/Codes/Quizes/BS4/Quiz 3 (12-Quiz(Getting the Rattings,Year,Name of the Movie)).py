import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class':'lister-list'})
trs = tbody.findAll('tr')
with open('imdbMoviesNameRating.csv', 'w') as f:
    for tr in trs:
        movieNametd = tr.find('td',{'class':'titleColumn'})
        ratingtd = tr.find('td',{'class':'ratingColumn'})
        f.write(movieNametd.a.string+ "," + movieNametd.span.string + "," +ratingtd.strong.string)
        f.write('\n')

