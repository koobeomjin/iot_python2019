name = input('이름을 입력하세요: ')

def search_visitor(name):
    with open('visitor.txt','r') as f:
        if f.read().find(name) != -1:
            print('{0}님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.'.format(name))
            return
        else:
            birth_date = input('생년월일을 입력하세요 (ex:801212) : ')
            registration(name, birth_date)

def registration(name, birth_date):
    print('{0}님 환영합니다. 아래 내용을 입력하셨습니다.'.format(name))
    print('{0}{1}'.format(name, birth_date))
    with open('visitor.txt', 'a')as f:
        f.write('\n{}''{}'.format(name,birth_date))


search_visitor(name)