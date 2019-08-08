import re
p = re.compile('Crow|Servo')
m = p.match('Nothing') # not match
print(m)
m = p.match('Nothing') # not match
print(m)
