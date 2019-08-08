import urllib.request
import datetime
import json

access_key = "q936T6OGEbMQSo27wG4c19Be3afao9GqAvRjH2VDi8z1pJZem6nrkC8%2BnupFTEfFS53H8XKE12nHdSMUwPaXDQ%3D%3D"
recommand_atmosphere_level = 1

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" %(datetime.datetime.now(), url))
        return None

def getFineDust():
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?"
    location = urllib.parse.quote('대구')
    parameters = "serviceKey="+access_key
    parameters += "&numOfRows=100"
    parameters += "&pageNo=1"
    parameters += "&sidoName="+location
    parameters += "&ver=1.3"
    parameters += "&_returnType=json"

    url = end_point + parameters

    retData = get_request_url(url)

    if (retData == None):
        return
    else:
        return json.loads(retData)

def main():
    g_Windows = True
    jsonResult = []

    jsonData = getFineDust()
    # for i in jsonData:
    #     data = jsonData['list'][0]
    #     for a in data:
    #         print(data[a])
    for data in  jsonData['list']:
        # print(data['stationName'])
        if (data['stationName']=='신암동'):
            if int(data['khaiGrade']) > int(recommand_atmosphere_level):
                if g_Windows == True:
                    sel = input('창문을 닫는것을 권장드립니다. 닫으시겠습니까?: ')
                    if sel == '1':
                        print('창문을 닫도록 하겠습니다.')
                    else:
                        print('더 나빠지기 전에 닫는 것을 추천드립니다.')
                else:
                    print('이미 창문이 닫혀있습니다.')


    with open ('미세먼지정보.json','w',encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

main()