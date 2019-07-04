#coding: cp949

age = 0

age = int(input("나이를 입력하세요"))

if age >= 0 and age <= 3:
    print("요금은 무료입니다.")
elif age > 3 and age <= 13:
    print("요금은 %d원 입니다." % 2000)
elif age > 13 and age <= 18:
    print("요금은 %d원 입니다." % 3000)
elif age > 18 and age <= 65:
    print("요금은 %d원 입니다." % 5000)
elif age > 65:
    print("요금은 무료입니다.")
