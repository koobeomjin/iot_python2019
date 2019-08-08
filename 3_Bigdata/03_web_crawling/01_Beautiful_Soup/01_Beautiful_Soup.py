from bs4 import BeautifulSoup

html='''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/1. Basic Concept.nhn?code=158191" title="1987">한국 영화 1987
        </a>
    </div>
</td>
'''

# a title <= 마우스 타겟시 설명 메세지 출력

soup = BeautifulSoup(html,'html.parser')

print("<soup>")
print(soup)
tag = soup.td
print("\ntag = soup.td")
print(tag)
tag = soup.div
print("\ntag=soup.div")
print(tag)

print("\ntag.attrs")
print(tag.attrs)
print("tag.string")