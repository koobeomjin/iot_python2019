#coding: cp949

coffee = 10
money = 0
coffee_price = 300

while True:
    money = int(input('���� �־��ּ���: '))
    if money < coffee_price:
        print('���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�.')
    else:
        coffee = coffee - 1
        if money > coffee_price:
            print('�Ž����� %d�� �ְ� '%(money-300), end='')
        print('Ŀ�Ǹ� �ݴϴ�')

    print('���� Ŀ���� ���� %d�� �Դϴ�.' %coffee)
    if coffee == 0:
        print('Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.')
        break
print('���α׷��� �����մϴ�.')