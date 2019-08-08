import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tag1 = soup.findAll('div', attrs={'class':'tit3'})
tag2 = soup.findAll('img', attrs={'class':"arrow"})
tag3 = soup.findAll('', attrs={'class':'range ac'})

def data_correction(org_text):
    if org_text == '\xa0':
        return 'N/A'
    return org_text

data = []

for i in range(len(tag1)):
    count = i+1
    point1 = data_correction(tag1[i].find('a').text)
    point2 = data_correction(tag2[i]['alt'])
    point3 = data_correction(tag3[i].text)

    if point2 == 'na': point2 = '0'
    elif point2 == 'up': point2 = '+'+point3
    elif point2 == 'down': point2 = '-'+point3

    data.append([count, point1, point2])

print(data)
