#coding: cp949
prompt = """�ȳ��ϼ���. ���� ���Կ� �湮�� �ּż� �����մϴ�!
1.�ֹ�
2.����
���Ͻô� �޴��� ������ �ּ���:"""

def input_ingredient():
    ingredient_list = []
    print('')
    print('������ġ�� ����ڽ��ϴ�.')
    print('')
    while True:
        ingredient = input('���Ͻô� ��Ḧ �Է��ϼ���: ')
        if ingredient == '����':
            return ingredient_list
        ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
    for i in ingredient_list:
        print('%s�� �߰��մϴ�.' % i)
    print('')
    print('�ֹ��Ͻ� ������ġ�� ��������ϴ�. ���ְ� �弼��.')
    print('')

while True:
    welcome = int(input(prompt))
    if welcome==2:
        break
    list = input_ingredient()
    make_sandwiches(list)