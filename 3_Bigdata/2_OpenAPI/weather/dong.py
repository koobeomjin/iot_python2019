import urllib.request
import datetime
import json
import time

access_key = "M6rSLzOg62CRjMyuRO2SRAvSpgrraiUqsty%2BO795jUFOyLRxvAOloMQP6P2cN1sPUguToMaUwqIrppHI0LNXTA%3D%3D"

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(),url))
        return None

def get_Weather_URL():
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?base_date=20190729&base_time=1150&nx=89&ny=91&_type=json&serviceKey="+access_key

    url = end_point+parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json():
    jsonData = get_Weather_URL()

    jsonData['respnose']['header']

    with open('동구_신암동_초단기예보조회_%s_%s.json' % (yyyymm,day_time),'w',encoding='utf-8')as outfile:
        retJson = json.dumps(json_weather_result, indent = 4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (yyyymm, day_time))

def get_Realtime_Weather_Info():
    Make_Weather_Json()

json_weather_result = []

x_coodinate = "89"
y_coodinate = "91"

get_Realtime_Weather_Info()