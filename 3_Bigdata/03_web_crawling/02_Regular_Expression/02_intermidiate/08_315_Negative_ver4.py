import re
file_name_list = ["foo.bar","autoexec.bat","sendmail.cf"]

# p = re.compile('.*[.].[^b].*$')
# p = re.compile('.*[.]([^b]..|.[^a].|..[^t]?)$')
# p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
p = re.compile('.*[.](?!bat$).*$')
p = re.compile('.*[.](?!bat$|bar$).*$')
for file_name in file_name_list:
    print(p.search(file_name))
