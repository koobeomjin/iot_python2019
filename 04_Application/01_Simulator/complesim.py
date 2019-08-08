import threading
import time
import ctypes
import urllib.request
import datetime
import json

g_Radiator = False
g_Gas_Valve = False
g_Door = False
g_Balcony_Windows = True
g_AI_Mode = False
schedule_cycle = 5

recommand_atmosphere_level = 1

access_key = "q936T6OGEbMQSo27wG4c19Be3afao9GqAvRjH2VDi8z1pJZem6nrkC8%2BnupFTEfFS53H8XKE12nHdSMUwPaXDQ%3D%3D"

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
    global g_Balcony_Windows
    jsonResult = []

    jsonData = getFineDust()
    # for i in jsonData:
    #     data = jsonData['list'][0]
    #     for a in data:
    #         print(data[a])
    for data in  jsonData['list']:
        # print(data['stationName'])
        if (data['stationName']=='신암동'):
            print('현재 대기환경지수:',data['khaiGrade'])
            if int(data['khaiGrade']) > int(recommand_atmosphere_level):
                if g_Balcony_Windows == True:
                    sel = input('창문을 닫는것을 권장드립니다. 닫으시겠습니까?(1.닫기): ')
                    if sel == '1':
                        print('창문을 닫도록 하겠습니다.')
                        g_Balcony_Windows = not g_Balcony_Windows
                    else:
                        print('더 나빠지기 전에 닫는 것을 추천드립니다.')
                elif g_Balcony_Windows == False:
                    print('이미 창문이 닫혀있습니다.')


    with open ('미세먼지정보.json','w',encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

def terminate_ai_mode():
    """Terminates a python thread from another thread:
    :param thread: a threading.Thread instance
    """
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyTreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)

    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsycExc failed")

def update_scheduler():
    while True:
        time.sleep(schedule_cycle)
        print(f"스케줄러 작동..   {schedule_cycle}초 주기")

while True:
    print("메뉴를 선택하세요")
    print("1. 장비 상태 조회")
    print("2. 인공지능 모드 변경")
    print("3. 대기환경지수 조회")
    print("4. 종료")

    menu_num = int(input("메뉴 입력: "))
    if(menu_num == 1):
        print("발코니 창문: ",end='')
        if g_Balcony_Windows == True: print("열림")
        else: print("닫힘")

        print("온열기: ",end='')
        if g_Radiator == True: print("작동")
        else: print("중지")

        print("현관문: ",end='')
        if g_Door == True: print("열림")
        else: print("닫힘")

        print("가스 벨브: ",end='')
        if g_Gas_Valve == True: print("열림")
        else: print("잠김")

    elif (menu_num == 2):
        print("인공지능 모드: ",end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode == True:
            ai_scheduler = threading.Thread(target=update_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print("작동 완료!")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass

            print("정지 완료!")
    elif menu_num == 3:
        main()
    else:
        print('작동을 중단합니다.')
        break