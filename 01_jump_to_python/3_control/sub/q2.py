#coding: cp949

age = 0

age1 = '����'
age2 = '���'
age3 = 'û�ҳ�'
age4 = '����'
age5 = '����'

fee1 = '2000'
fee2 = '3000'
fee3 = '5000'

age = int(input("���̸� �Է��ϼ���"))

if age >= 0 and age <= 3:
    print("������ ����� %s�̸� ����� �����Դϴ�." %age1)
elif age > 3 and age <= 13:
    print("������ ����� %s�̸� ����� %s�� �Դϴ�." %(age2, fee1))
elif age > 13 and age <= 18:
    print("������ ����� %s�̸� ����� %s�� �Դϴ�." %(age3, fee2))
elif age > 18 and age <= 65:
    print("������ ����� %s�̸� ����� %s�� �Դϴ�." %(age4, fee3))
elif age > 65:
    print("������ ����� %s�̸� ����� �����Դϴ�." %age5)
elif age < 0:
    print("�ٽ� �Է��ϼ���")
