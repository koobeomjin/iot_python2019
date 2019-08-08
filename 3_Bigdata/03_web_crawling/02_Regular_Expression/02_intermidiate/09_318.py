import re

p = re.compile('(blue|white|red)')
print(p.sub('color','blue socks and red shoes'))
print(p.sub('color','blue socks and red shoes'))
print(p.sub('color','blue socks and red shoes'))
print(p.sub('color','blue socks and red shoes'))
