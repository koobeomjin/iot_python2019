import random
# BMI(체질량 지수)를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"

# 출력파일 준비하기
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\r\n")
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)

#무작위로 데이터 생성하기
cnt = {"thin":0, "normal":0, "fat":0}
for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(35, 80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h, w, label))
fp.close()
print("ok,",cnt)
