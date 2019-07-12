while True:
    i = 1
    j = 1
    k = 1
    odd_num = int(input('홀수를 입력하세요(0 <- 종료): '))
    if odd_num == 0:
        print('\n마름모 출력 프로그램을 이용해 주셔서 감사합니다.')
        break
    elif odd_num % 2 == 0:
        print('짝수를 입력하셨습니다. 홀수를 입력해 주세요.')
    else:
        print(' ' + '-' * odd_num)
        repitition = int((odd_num/2 + 1))
        i = repitition - 1
        while repitition >= j:
            print('|' + ' ' * i + '*' * k + ' ' * i + '|')
            i -= 1
            j += 1
            k += 2
        j = 1
        k -= 2
        i += 1
        while repitition > j:
            i += 1
            j += 1
            k -= 2
            print('|' + ' ' * i + '*' * k + ' ' * i + '|')
        print(' ' + '-' * odd_num)