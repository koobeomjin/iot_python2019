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
elif age > 13 and age <= 18:
    print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age3, fee2))
elif age > 18 and age <= 65:
    print("귀하의 등급은 %s이며 요금은 %s원 입니다." %(age4, fee3))
elif age > 65:
    print("귀하의 등급은 %s이며 요금은 무료입니다." %age5)
elif age < 0:
    print("다시 입력하세요")
