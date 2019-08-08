import re
p = re.compile('[a-z]+')
m = p.match('python')
# m = p.match('3 python')
print(m)
if m:
    print('Match found:', m.group())
else:
    print('No Match')

p = re.compile('[a-z]+')
m = p.match('3 python')
print(m)