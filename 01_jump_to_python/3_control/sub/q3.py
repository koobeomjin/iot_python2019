#coding: cp949

age = 0

age1 = '유아'
age2 = '어린이'
age3 = '청소년'
age4 = '성인'
age5 = '노인'

fee1 = '2000'
fee2 = '3000'
fee3 = '5000'

age = int(input("나이를 입력하세요"))

if age >= 0 and age <= 3:
    print("귀하의 등급은 %s이며 요금은 무료입니다." %age1)
elif age > 3 and age <= 13:
    print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age2, fee1))

    input_money = int(input('요금을 입력하세요. '))
    result = input_money - int(fee1)

    if input_money > int(fee1):
        print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %result)
    if input_money == int(fee1):
        print('감사합니다. 티켓을 발행합니다.' %result)
    if input_money < int(fee1):
        print('입력하신 금액에 %d원이 부족합니다. 입력하신 금액 %d원을 반환합니다.' %(result * -1, input_money))

elif age > 13 and age <= 18:
    print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age3, fee2))

    input_money = int(input('요금을 입력하세요. '))
    result = input_money - int(fee2)

    if input_money > int(fee2):
        print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %result)
    if input_money == int(fee2):
        print('감사합니다. 티켓을 발행합니다.' %result)
    if input_money < int(fee2):
        print('입력하신 금액에 %d원이 부족합니다. 입력하신 금액 %d원을 반환합니다.' %(result * -1, input_money))

elif age > 18 and age <= 65:
    print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age4, fee3))

    input_money = int(input('요금을 입력하세요. '))
    result = input_money - int(fee3)

    if input_money > int(fee3):
        print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %result)
    if input_money == int(fee3):
        print('감사합니다. 티켓을 발행합니다.' %result)
    if input_money < int(fee3):
        print('입력하신 금액에 %d원이 부족합니다. 입력하신 금액 %d원을 반환합니다.' %(result * -1, input_money))

elif age > 65:
    print("귀하의 등급은 %s이며 요금은 무료입니다." %age5)
elif age < 0:
    print("다시 입력하세요")
