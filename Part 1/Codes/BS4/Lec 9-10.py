from bs4 import BeautifulSoup
html = '<b id="xyz" class="abc 123"> Hello World</b><span></span><span></span>'
soup = BeautifulSoup(html, 'html.parser', multi_valued_attributes=None)
tag = soup.b

print(tag['id'])
print(tag['class'])
print(tag.attrs)
print(tag)
tag['id'] = 'HELLO'
tag['class'] = 'World'
print(tag)
print(tag['class'])

