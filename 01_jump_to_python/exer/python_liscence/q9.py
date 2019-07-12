with open('sample.txt', 'r') as f:
    number_list = []
    temp_list = f.readlines()
    for temp in temp_list:
        number_list.append(temp.rstrip())

result = 0
for i in number_list:
    result = result + int(i)
print(result/10)