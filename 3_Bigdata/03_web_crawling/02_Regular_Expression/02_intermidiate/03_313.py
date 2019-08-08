import re
p = re.compile(r'(\w+)\s+(\d+)[-](\d+)[-](\d+)')

m = p.match("park 010-1234-5678")
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
# print(m.group(5)) <= 매칭이 되는 그룹이 없기 때문에 에러