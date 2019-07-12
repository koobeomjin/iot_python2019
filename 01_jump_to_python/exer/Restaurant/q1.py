class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __del__(self):
        print('%s 레스토랑 문닫습니다.' %self.name)


    def describe_restaurant(self):
        print('저희 레스토랑 명칭은 %s이고 %s 전문점입니다.' %(self.name, self.type))

    def open_restaurant(self):
        print('저희 %s 레스토랑이 오픈했습니다.\n'%(self.name))

info = input('레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분): ')
name_list = info.split()

my_retaurant = Restaurant(name_list[0],name_list[1])
my_retaurant.describe_restaurant()
my_retaurant.open_restaurant()

