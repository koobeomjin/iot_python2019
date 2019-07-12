input_number = input('숫자를 입력하세요 (콤마로 구분합니다.): ')
list = input_number.split(',')

result = 0

for i in list:
    result = result+int(i)
print(result)