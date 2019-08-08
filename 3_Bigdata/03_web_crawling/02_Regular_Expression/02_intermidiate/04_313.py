import re
p = re.compile(r'(\b\w+)\s+\1')
# p = re.compile('(\b\w+)\s+\1')
print(p.search('Paris in the spring. It was really great').group())