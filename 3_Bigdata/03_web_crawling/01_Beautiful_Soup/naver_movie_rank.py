import urllib.request
from bs4 import BeautifulSoup

html = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
print(soup.prettify())

tags = soup.findAll('div', attrs = {'class':'tit3'})
up_down = soup.find('img', attrs = {'src':
'https://imgmovie.naver.net/imgmovie/2007/img/common/icon_na_1.gif'})

