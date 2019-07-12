def check(e):
    for i in range(0,10):
        if e.count(str(i)) == 1:
            pass
        else:
            return 'false'
    return 'true'
a1 = input('0~9사이의 숫자를 입력하세요: ')
a1 = a1.split()
for e in a1:
    b = check(e)
    print(b)