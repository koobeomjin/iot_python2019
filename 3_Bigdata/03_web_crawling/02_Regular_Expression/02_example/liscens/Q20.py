import re

data="""
park@naver.com
kim@daum.net
lee@myhome.co.kr
qhawks1672@gmail.com
jasnasnf@nvanv.go.kr
ansnf22@hanmail.net
ansnf22@hanmail.ko.kr
"""

pat = re.compile(".*[@].*[.](?=com|net).*",re.MULTILINE)
match = pat.findall(data)

for match_domain in match:
    print(match_domain)