#coding: cp949
age = 0
age1 = '����'
age2 = '���'
age3 = 'û�ҳ�'
age4 = '����'
age5 = '����'
choice = 0
fee1 = '2000'
fee2 = '3000'
fee3 = '5000'
count_a = 0
count_b = 0
free_ticket = 5
discount_ticket = 3
prompt = '���� ������ �����ϼ���\n'"""
1.����
2.���� ���� �ſ�ī��\n
"""
while True:
    age = int(input("���̸� �Է��ϼ���"))
    if age >= 0 and age <= 3:
      print("������ ����� %s�̸� ����� �����Դϴ�." %age1)
      print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif age > 3 and age <= 13:
      print("������ ����� %s�̸� ����� %s�� �Դϴ�." %(age2, fee1))
      choice = int(input(prompt))
      if choice == 1:
          input_money = int(input('���� �� ����� �Է��ϼ���. '))
          result = input_money - int(fee1)
          if input_money > int(fee1):
              print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.' %result)
          if input_money == int(fee1):
              print('�����մϴ�. Ƽ���� �����մϴ�.')
          if input_money < int(fee1):
              print('�Է��Ͻ� �ݾ׿� %d���� �����մϴ�. �Է��Ͻ� �ݾ� %d���� ��ȯ�մϴ�.' %(result * -1, input_money))
      elif choice == 2:
          print('���� ���� �ſ�ī�� ������ �޾Ƽ� %f�� �����Ǿ����ϴ�.' %(int(fee1) * 0.9))
    elif age > 13 and age <= 18:
        print("������ ����� %s�̸� ����� %s�� �Դϴ�." %(age3, fee2))
        choice = int(input(prompt))
        if choice == 1:
            input_money = int(input('���� �� ����� �Է��ϼ���. '))
            result = input_money - int(fee2)
            if input_money > int(fee2):
                print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.' %result)
            if input_money == int(fee2):
                print('�����մϴ�. Ƽ���� �����մϴ�.')
            if input_money < int(fee2):
                print('�Է��Ͻ� �ݾ׿� %d���� �����մϴ�. �Է��Ͻ� �ݾ� %d���� ��ȯ�մϴ�.' %(result * -1, input_money))
        elif choice == 2:
            print('���� ���� �ſ�ī�� ������ �޾Ƽ� %f�� �����Ǿ����ϴ�.' %(int(fee2) * 0.9))
    elif age > 18 and age <= 65:
        print("������ ����� %s�̸� ����� %s�� �Դϴ�." %(age4, fee3))
        choice = int(input(prompt))
        if choice == 1:
            input_money = int(input('���� �� ����� �Է��ϼ���. '))
            result = input_money - int(fee3)
            if input_money > int(fee3):
                print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.' %result)
            if input_money == int(fee3):
                print('�����մϴ�. Ƽ���� �����մϴ�.')
            if input_money < int(fee3):
                print('�Է��Ͻ� �ݾ׿� %d���� �����մϴ�. �Է��Ͻ� �ݾ� %d���� ��ȯ�մϴ�.' %(result * -1, input_money))
        elif choice == 2:
            print('���� ���� �ſ�ī�� ������ �޾Ƽ� %f�� �����Ǿ����ϴ�.' %(int(fee3) * 0.9))
    elif age > 65:
        print("������ ����� %s�̸� ����� �����Դϴ�." %age5)
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif age < 0:
        print("�ٽ� �Է��ϼ���")
    if age >= 4 and age <= 65:
        count_a +=1
        count_b +=1
        if count_a == 7:
            if free_ticket > 0:
                print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� Ƽ�� %d��" %(free_ticket - 1))
                free_ticket -= 1
                count_a = 0
        elif count_b == 4:
            if discount_ticket > 0:
                print("�����մϴ�. ���� ȸ���� ���� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� Ƽ�� %d��" %(discount_ticket-1))
                discount_ticket -= 1
                count_b=0