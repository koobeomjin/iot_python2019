import urllib.request
import datetime
import json

g_Radiator = False
g_Gas_Valve = False
g_Door = False
g_Balcony_Windows = False
g_AI_Mode = False

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

def print_main_menu():
    print("\n1. 장비 상태 확인")
    print("2. 장비 제어")
    print("3. 스마트 모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, device_status):
    print("%s 상태: " %device_name, end="")
    if device_status == True: print("작동")
    else: print("정지")

def check_device_status():
    print('')
    print_device_status('난방기', g_Radiator)
    print_device_status('가스 벨브', g_Gas_Valve)
    print_device_status('발코니 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태를 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스 벨브")
    print("3. 발코니 창문")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()

def get_realtime_weather_info():
    print("자! 메뉴얼을 보고 작성해 보세요!")

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print('4. 대기환경지수 조회하기')
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ",end='')
        if g_AI_Mode == True:
            print("작동 완료!")
        else:
            print("중지!")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ",end='')
        if g_AI_Mode == True: print("작동")
        else: print("중지")

    elif menu_num == 3:
        get_realtime_weather_info()

    elif menu_num == 4:
        main()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if (menu_num == 1):
        check_device_status()
    elif (menu_num == 2):
        control_device()
    elif (menu_num == 3):
        smart_mode()
    elif (menu_num == 4):
        break