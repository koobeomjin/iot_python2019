from urllib.parse import quote
from urllib.request import Request, urlopen
import ssl
import json

kor_url = quote(input('주소와 번지수를 입력하세요: '))
url = ('https://maps.googleapis.com/maps/api/geocode/json?address='+kor_url+'&key=''AIzaSyDyugO7TbFbbjzFDjch8YJ56CF05O4JnLE''&language=ko')

req = Request(url, headers={ 'X-Mashape-Key': 'AIzaSyDyugO7TbFbbjzFDjch8YJ56CF05O4JnLE' })
ssltext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
company_addr_json = urlopen(req, context=ssltext).read().decode('utf8')

addr = json.loads(company_addr_json)

addr_detail = addr['results'][0]

#전체 주소
full_addr = addr_detail['formatted_address']

#시도 주소
city_addr1 = addr_detail['address_components'][4]['long_name']

#구 주소
city_addr = addr_detail['address_components'][3]['long_name']

#동,읍 주소
go_addr = addr_detail['address_components'][2]['long_name']

#대로 주소
dong_addr = addr_detail['address_components'][1]['long_name']

#번지 주소
bunji_addr = addr_detail['address_components'][0]['long_name']

# print(addr_detail)
print(full_addr)
print(city_addr1)
print(city_addr)
print(go_addr)
print(dong_addr)
print(bunji_addr)

