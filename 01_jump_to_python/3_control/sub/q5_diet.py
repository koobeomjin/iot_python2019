#coding: cp949
age = 0
age1 = '유아'
age2 = '어린이'
age3 = '청소년'
age4 = '성인'
age5 = '노인'
choice = 0
fee1 = '2000'
fee2 = '3000'
fee3 = '5000'
count_a = 0
count_b = 0
free_ticket = 5
discount_ticket = 3
prompt = '결제 유형을 선택하세요\n'"""
1.현금
2.공원 전용 신용카드\n
"""
while True:
    age = int(input("나이를 입력하세요"))
    if age >= 0 and age <= 3:
      print("귀하의 등급은 %s이며 요금은 무료입니다." %age1)
      print("감사합니다. 티켓을 발행합니다.")
    elif age > 3 and age <= 13:
      print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age2, fee1))
      choice = int(input(prompt))
      if choice == 1:
          input_money = int(input('투입 할 요금을 입력하세요. '))
          result = input_money - int(fee1)
          if input_money > int(fee1):
              print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %result)
          if input_money == int(fee1):
              print('감사합니다. 티켓을 발행합니다.')
          if input_money < int(fee1):
              print('입력하신 금액에 %d원이 부족합니다. 입력하신 금액 %d원을 반환합니다.' %(result * -1, input_money))
      elif choice == 2:
          print('공원 전용 신용카드 할인을 받아서 %f원 결제되었습니다.' %(int(fee1) * 0.9))
    elif age > 13 and age <= 18:
        print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age3, fee2))
        choice = int(input(prompt))
        if choice == 1:
            input_money = int(input('투입 할 요금을 입력하세요. '))
            result = input_money - int(fee2)
            if input_money > int(fee2):
                print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %result)
            if input_money == int(fee2):
                print('감사합니다. 티켓을 발행합니다.')
            if input_money < int(fee2):
                print('입력하신 금액에 %d원이 부족합니다. 입력하신 금액 %d원을 반환합니다.' %(result * -1, input_money))
        elif choice == 2:
            print('공원 전용 신용카드 할인을 받아서 %f원 결제되었습니다.' %(int(fee2) * 0.9))
    elif age > 18 and age <= 65:
        print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age4, fee3))
        choice = int(input(prompt))
        if choice == 1:
            input_money = int(input('투입 할 요금을 입력하세요. '))
            result = input_money - int(fee3)
            if input_money > int(fee3):
                print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %result)
            if input_money == int(fee3):
                print('감사합니다. 티켓을 발행합니다.')
            if input_money < int(fee3):
                print('입력하신 금액에 %d원이 부족합니다. 입력하신 금액 %d원을 반환합니다.' %(result * -1, input_money))
        elif choice == 2:
            print('공원 전용 신용카드 할인을 받아서 %f원 결제되었습니다.' %(int(fee3) * 0.9))
    elif age > 65:
        print("귀하의 등급은 %s이며 요금은 무료입니다." %age5)
        print("감사합니다. 티켓을 발행합니다.")
    elif age < 0:
        print("다시 입력하세요")
    if age >= 4 and age <= 65:
        count_a +=1
        count_b +=1
        if count_a == 7:
            if free_ticket > 0:
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여 티켓 %d장" %(free_ticket - 1))
                free_ticket -= 1
                count_a = 0
        elif count_b == 4:
            if discount_ticket > 0:
                print("축하합니다. 연간 회원권 구매 이벤트에 당첨되었습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 티켓 %d장" %(discount_ticket-1))
                discount_ticket -= 1
                count_b=0
