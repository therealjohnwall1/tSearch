from bs4 import BeautifulSoup

path = 'random.html'
html = open(path, 'r')
soup = BeautifulSoup(html,'lxml')

text = soup.get_text()

print(text.replace('\n','').replace('\t',''))

links = soup.find_all('a')
for link in links:
    print(link.get('href'))



