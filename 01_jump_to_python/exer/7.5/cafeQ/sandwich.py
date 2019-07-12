#coding: cp949
prompt = """안녕하세요. 저희 가게에 방문해 주셔서 감사합니다!
1.주문
2.종료
원하시는 메뉴를 선택해 주세요:"""

def input_ingredient():
    ingredient_list = []
    print('')
    print('샌드위치를 만들겠습니다.')
    print('')
    while True:
        ingredient = input('원하시는 재료를 입력하세요: ')
        if ingredient == '종료':
            return ingredient_list
        ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
    for i in ingredient_list:
        print('%s를 추가합니다.' % i)
    print('')
    print('주문하신 샌드위치를 만들었습니다. 맛있게 드세요.')
    print('')

while True:
    welcome = int(input(prompt))
    if welcome==2:
        break
    list = input_ingredient()
    make_sandwiches(list)