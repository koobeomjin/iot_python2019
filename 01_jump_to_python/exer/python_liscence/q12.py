result = 0
try:
    [1,2,3][3]
    "a"+1
    4/0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
     result += 3
finally:
    result += 4

print(result)
print('result = 7, 1번째 줄의 인덱스 구문에서 오류가 발생하므로 무시하고 진행함')