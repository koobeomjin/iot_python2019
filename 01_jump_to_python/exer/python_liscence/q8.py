with open('abc.txt', 'r')as f:
    abc = []
    a = f.readlines()

    for temp in a:
        abc.append(temp.rstrip())
abc.reverse()

f = open('abc.txt', 'w')
f.write('\n'.join(abc))
f.close()