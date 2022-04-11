import requests
from bs4 import BeautifulSoup

movieName = input('Enter Movie Name: ')
movieName = movieName.lower()

res = requests.get('https://www.imdb.com/chart/top/')
html = res.text

soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')
for tr in trs:
    td = tr.find('td', {'class': 'titleColumn'})
    imdbMovieName = td.a.string.strip().lower()
    if imdbMovieName == movieName:
        movieId = td.a['href']
        movieUrl = f'https://www.imdb.com/{movieId}'
        res2 = requests.get(movieUrl)
        html = res2.text
        soup2 = BeautifulSoup(html, 'html.parser')
        summary = soup2.find('div', {'class': 'credit_summary_item'})
        dirID = summary.a['href']
        dirUrl = f'https://www.imdb.com/{dirID}'
        print("Dir Name: ",summary.a.string)
        res3 = requests.get(dirUrl)
        html = res3.text
        soup3 = BeautifulSoup(html, 'html.parser')
        knownfor = soup3.find('div', {'id': 'knownfor'})
        movieDivs = knownfor.findAll('div', {'class': 'knownfor-title'})
        for div in movieDivs:
            moviediv = div.find('div', {'class': 'knownfor-title-role'})
            print(moviediv.a.string)

        break












