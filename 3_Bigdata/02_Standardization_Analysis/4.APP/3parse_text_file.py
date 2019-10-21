import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

message = {}
notes = []
with open(input_file, 'r', newline='') as text_file:
    for row in text_file:
        if '[Note]' in row:
            row_list = row.split(' ', 4) # 두번째 인자는 MAX split의 수 5번쨰 이후는 split하지 않는다.
            day = row_list[0].strip()
            note = row_list[4].strip('\n').strip()
            if note not in notes:
                notes.append(note)
            if day not in message:
                message[day] = {}
            if note not in message[day]:
                message[day][note] = 1
            else:
                message[day][note] += 1

filewirter = open(output_file, 'w', newline='')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print(header)
filewirter.write(header)
for day, day_value in message.items():
    row_of_output = []
    row_of_output.append(day)
    for index in range(len(notes)):
        if notes[index] in day_value.keys():
            row_of_output.append(day_value[notes[index]])
        else:
            row_of_output.append(0)
    output = ','.join(map(str,row_of_output)) + '\n'
    print(output)
    filewirter.write(output)
filewirter.close()