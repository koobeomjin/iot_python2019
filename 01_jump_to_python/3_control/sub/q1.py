#coding: cp949

age = 0

age = int(input("���̸� �Է��ϼ���"))

if age >= 0 and age <= 3:
    print("����� �����Դϴ�.")
elif age > 3 and age <= 13:
    print("����� %d�� �Դϴ�." % 2000)
elif age > 13 and age <= 18:
    print("����� %d�� �Դϴ�." % 3000)
elif age > 18 and age <= 65:
    print("����� %d�� �Դϴ�." % 5000)
elif age > 65:
    print("����� �����Դϴ�.")
