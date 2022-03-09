import requests
for i in range(1, 12):
    print("Page: ", i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    html = r.text
    with open('quotes.txt', 'a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
                line = line.strip()
                f.write(line)
                f.write("\n")
