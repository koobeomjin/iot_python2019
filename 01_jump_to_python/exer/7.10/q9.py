import sys
a = []
total = 0
a = sys.argv[1:]
for i in a:
    total += int(i)

print(total)