import requests
import json
with open('superstats.csv','w') as f:
    for i in range(1,3):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}'
        res = requests.get(url)
        data = res.text
        data = json.loads(data)
        for headline in data:
            _headline = headline['headline']
            _headline = _headline.replace(',', '|')
            f.write(_headline)
            f.write('\n')