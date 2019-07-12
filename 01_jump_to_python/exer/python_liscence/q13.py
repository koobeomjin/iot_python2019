def DashInsert(input_number):
    H = 0
    Z = 0
    c = 0

    for i in input_number:
        i = int(i)
        if i%2 == 1:
            H = H+1
            Z = 0
        elif i%2 == 0:
            Z = Z+1
            H = 0
        if H == 2:
            H = 1
            Z = 0
            input_number =  input_number[:c]+'-'+input_number[c:]
            c = c+1
        elif Z == 2:
            Z = 1
            H = 0
            input_number =  input_number[:c]+'*'+input_number[c:]
            c = c+1
        c = c+1

    return input_number

input_number = input('숫자를 입력하세요: ')


a = DashInsert(input_number)

print(a)
