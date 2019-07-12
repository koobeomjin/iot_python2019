a = range(1,1000)
r = 0
total = 0
for r in a:
    if r%3 == 0 or r%5 == 0:
        total += r
print('3과 5의 배수의 총합 : %d' %total)