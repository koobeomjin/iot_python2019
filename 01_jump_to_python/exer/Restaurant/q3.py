class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.select = 0
        self.number = 0

    # def __del__(self):
    #     print('%s 레스토랑 문닫습니다.' % self.name)

    def describe_restaurant(self):
        print('저희 레스토랑 명칭은 %s이고 %s 전문점입니다.' %(self.name, self.type))

    def open_restaurant(self):
        print('저희 %s 레스토랑이 오픈했습니다.\n'%(self.name))
        choice = input('레스토랑을 오픈하시겠습니까? (y/n):')
        if choice == "y":
            my_retaurant.reset_number_served()
        else:
            print('영업을 종료하겠습니다.')

    def increment_number_served(self):
        self.number = self.number + int(self.select)

    def reset_number_served(self):
        while True:
            self.select = input("어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) :")
            if self.select == "-1":
                print('안녕히 가세요')
                exit()
            elif self.select == "0":
                print('손님 카운팅을 0으로 초기화 하였습니다.')
                self.number = 0
            elif self.select == "p":
                my_retaurant.check_customer_number()
            else:
                print(f'손님 {self.select}명 들어오셨습니다. 자리를 안내해 드리겠습니다.')
                my_retaurant.increment_number_served()
            print("")

    def check_customer_number(self):
        print('지금까지 총 %d명 손님께서 오셨습니다.' %self.number)

info = input('레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분): ')
name_list = info.split()
my_retaurant = Restaurant(name_list[0],name_list[1])
my_retaurant.describe_restaurant()
my_retaurant.open_restaurant()