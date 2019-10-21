import urllib.request
import datetime
import json
import math

access_key = "q936T6OGEbMQSo27wG4c19Be3afao9GqAvRjH2VDi8z1pJZem6nrkC8%2BnupFTEfFS53H8XKE12nHdSMUwPaXDQ%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s"%(datetime.datetime.now(),url))
        return None


def getTourPointVisitor():
    end_point = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList"

    parameters = "?serviceKey="+access_key
    parameters += "%3D%3D&pageNo=1&numOfRows=20&MobileApp=AppTest&MobileOS=ETC&arrange=A&contentTypeId=12&areaCode=4&sigunguCode=4&listYN=Y"

    url=end_point+parameters+"%_type=json"

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


def getTourPointData(item, jsonResult):
    add1 = '' if 'addr1' not in item.keys() else item['addr1']
    add2 = '' if 'addr2' not in item.keys() else item['addr2']
    areacode = 0 if 'areacode' not in item.keys() else item['areacode']
    cat1 = '' if 'cat1' not in item.keys() else item['cat1']
    cat2 = '' if 'cat2' not in item.keys() else item['cat2']
    cat3 = '' if 'cat3' not in item.keys() else item['cat3']
    contentid = '' if 'contentid' not in item.keys() else item['contentid']
    contenttypeid = 0 if 'contenttypeid' not in item.keys() else item['contenttypeid']
    createdtime = '' if 'createdtime' not in item.keys() else item['createdtime']
    firstimage = '' if 'firstimage' not in item.keys() else item['firstimage']
    firstimage2 = '' if 'firstimage2' not in item.keys() else item['firstimage2']
    mapx = 0 if 'mapx' not in item.keys() else item['mapx']
    mapy = 0 if 'mapy' not in item.keys() else item['mapy']
    mlevel = 0 if 'mlevel' not in item.keys() else item['mlevel']
    modifiedtime = '' if 'modifiedtime' not in item.keys() else item['modifiedtime']
    readcount = 0 if 'readcount' not in item.keys() else item['readcount']
    sigungucode = 0 if 'sigungucode' not in item.keys() else item['sigungucode']
    title = '' if 'title' not in item.keys() else item['title']
    zipcode = 0 if 'zipcode' not in item.keys() else item['zipcode']

    jsonResult.append({'add1' : add1, 'add2' : add2, 'areacode' : areacode, 'cat1' : cat1,
    'cat2' : cat2, 'cat3': cat3, 'contentid' : contentid, 'contenttypeid' : contenttypeid,
    'createdtime' : createdtime, 'firstimage' : firstimage, 'firstimage2' : firstimage2,
    'mapx' : mapx, 'mapy' : mapy, 'mlevel' : mlevel, 'modifiedtime' : modifiedtime,
    'readcount' : readcount, 'sigungucode' : sigungucode, 'title' : title, 'zipcode' : zipcode})

    return

