import csv
import os

base_repository_name = 'A_Bigdata_Repository'
dir_delimeter = '/'
file_name = '시뮬레이션_서울특별시_서대문형무소역사관_방문객'
file_format = 'csv'
initial_file_name = f'{base_repository_name}{dir_delimeter}{file_name}1.{file_format}'
simulation_count = 100
simulation_data = ['1141','서대문구','서울특별시','서대문형무소역사관','8','4392','75348']
file_size_limit = 10000
is_header = False
is_first = False

def getTourPointData(filewriter):
    filewriter.writerow(simulation_data)
    return

if not os.path.exists(base_repository_name):
    os.mkdir(base_repository_name)

def get_dest_file_name(file_index):
    global is_header
    dest_file_name = f'{base_repository_name}{dir_delimeter}{file_name}{str(file_index)}.{file_format}'

    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"'{dest_file_name}' file size: {file_size}")
        print(f"파일당 size 제한: {file_size_limit}")

        if file_size > file_size_limit:
            dest_file_name = f'{base_repository_name}{dir_delimeter}{file_name}{str(file_index+1)}.{file_format}'
            is_header = True
        else:
            is_header = False
    except:
        pass
    return dest_file_name

def save_file(index):
    dest_file_name = get_dest_file_name(index)

    csv_out_file = open(dest_file_name, 'a', newline='')
    filewriter = csv.writer(csv_out_file)

    if is_header == True or is_first == True:
        header_list = ['addrCd', 'gungu', 'sido', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
        filewriter.writerow(header_list)

    for index in range(simulation_count):
        getTourPointData(filewriter)
    csv_out_file.close()

def file_count():
    index = len(os.listdir(base_repository_name))
    return index


B_base_repository_name = 'B_Bigdata_Repository'
B_dir_delimeter = '/'
B_file_name = '시뮬레이션_서울특별시_서대문형무소역사관_방문객'
B_file_format = 'excel'
B_initial_file_name = f'{B_base_repository_name}{B_dir_delimeter}{B_file_name}1.{B_file_format}'
B_simulation_count = 100
B_simulation_data = ['1141','서대문구','서울특별시','서대문형무소역사관','8','4392','75348']
B_file_size_limit = 10000
B_is_header = False
B_is_first = False

def B_getTourPointData(B_filewriter):
    B_filewriter.writerow(B_simulation_data)
    return

if not os.path.exists(B_base_repository_name):
    os.mkdir(B_base_repository_name)

def B_get_dest_file_name(B_file_index):
    global B_is_header
    B_dest_file_name = f'{B_base_repository_name}{B_dir_delimeter}{B_file_name}{str(B_file_index)}.{B_file_format}'

    try:
        B_file_size = os.path.getsize(B_dest_file_name)
        print(f"'{B_dest_file_name}' file size: {B_file_size}")
        print(f"파일당 size 제한: {B_file_size_limit}")

        if B_file_size > B_file_size_limit:
            B_dest_file_name = f'{B_base_repository_name}{B_dir_delimeter}{B_file_name}{str(B_file_index+1)}.{B_file_format}'
            B_is_header = True
        else:
            B_is_header = False
    except:
        pass
    return B_dest_file_name

def B_save_file(B_index):
    B_dest_file_name = B_get_dest_file_name(B_index)

    B_csv_out_file = open(B_dest_file_name, 'a', newline='')
    B_filewriter = csv.writer(B_csv_out_file)

    if B_is_header == True or B_is_first == True:
        B_header_list = ['addrCd', 'gungu', 'sido', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
        B_filewriter.writerow(B_header_list)

    for B_index in range(B_simulation_count):
        B_getTourPointData(B_filewriter)
    B_csv_out_file.close()

def B_file_count():
    B_index = len(os.listdir(B_base_repository_name))
    return B_index


print("경량화 빅데이터 저장소 시뮬레이션 v1.0 - 구범진")
while True:
    print("\n\t< 메인 메뉴 >")
    print("\t1. 작업수행")
    print("\t2. 환경설정")
    print("\t3. 종료")
    menu = int(input("\t메뉴를 선택하세요 : "))

    if menu == 1:
        print('\n\t1. TypeA 데이터 수집')
        print('\t2. TypeB 데이터 수집')
        print('\t3. 이전 메뉴')
        act_num = int(input('\t선택하여 주세요: '))
        if act_num == 1:
            if not os.path.exists(base_repository_name):
                os.mkdir(base_repository_name)

            if not os.path.exists(initial_file_name):
                is_first = True
                save_file(1)
            else:
                save_file(file_count())
            print('\n\t작업을 수행하였습니다.\n')
        elif act_num == 2:
            if not os.path.exists(B_base_repository_name):
                os.mkdir(B_base_repository_name)

            if not os.path.exists(B_initial_file_name):
                B_is_first = True
                B_save_file(1)
            else:
                B_save_file(B_file_count())
            print('\n\t작업을 수행하였습니다.\n')
        else:
            continue
    elif menu == 2:
        print(f'\n\t1. A Base Repository명 : {base_repository_name}')
        print(f'\t2. A 파일명 : {file_name}')
        print(f'\t3. A 포멧 : {file_format}')
        print(f'\t4. 데이터 용량 제한 : {file_size_limit}')
        print(f'\t5. B_Base Repository명 : {B_base_repository_name}')
        print(f'\t6. B 파일명 : {B_file_name}')
        print(f'\t7. B 포멧 : {B_file_format}')
        print(f'\t8. B 데이터 용량 제한 : {B_file_size_limit}')
        print('\t9. 이전메뉴')
        menu2 = int(input('\t메뉴를 선택하세요: '))
        if menu2 == 1:
            print('\t파일A의 저장위치의 변경을 희망하셨습니다.')
            change_repository_name = input('\t변경을 원하시는 A폴더명을 입력하세요 : ')
            base_repository_name = change_repository_name
            print('\n\t작업을 수행하였습니다.\n')
            continue
        elif menu2 == 2:
            print('\t파일A의 파일명 변경을 희망하셨습니다.')
            change_file_name = input('\t바꾸실 파일명을 입력하세요 : ')
            file_name = change_file_name
            print('\n\t작업을 수행하였습니다.\n')
        elif menu2 == 3:
            print('\t파일A의 포멧 형식 변경을 희망하셨습니다.')
            change_format = input('\t변경하실 포멧 형식을 입력하세요: ')
            file_format = change_format
            print('\n\t작업을 수행하였습니다.\n')
        elif menu2 == 4:
            print('\t파일A의 데이터 용량 제한 변경을 희망하셨습니다.')
            change_file_size_limit = input('\t변경하실 데이터 용량 제한을 설정해주세요: ')
            file_size_limit = change_file_size_limit
            print('\n\t작업을 수행하였습니다.\n')
        elif menu2 == 5:
            print('\t파일B의 저장위치 변경을 희망하셨습니다.')
            change_B_repository_name = input('\t바꾸실 폴더명을 입력하세요 : ')
            B_base_repository_name = change_B_repository_name
            print('\n\t작업을 수행하였습니다.\n')
            continue
        elif menu2 == 6:
            print('\t파일B의 파일명 변경을 희망하셨습니다.')
            change_B_file_name = input('\t바꾸실 파일명을 입력하세요 : ')
            B_file_name = change_B_file_name
            print('\n\t작업을 수행하였습니다.\n')
        elif menu2 == 7:
            print('\t파일B의 포멧 형식 변경을 희망하셨습니다.')
            change_B_format = input('\t변경하실 포멧 형식을 입력하세요: ')
            B_file_format = change_B_format
            print('\n\t작업을 수행하였습니다.\n')
        elif menu2 == 8:
            print('\t파일B의 데이터 용량 제한 변경을 희망하셨습니다.')
            change_B_file_size_limit = input('\t변경하실 데이터 용량 제한을 설정해주세요: ')
            B_file_size_limit = change_B_file_size_limit
            print('\n\t작업을 수행하였습니다.\n')
        elif menu2 == 9:
            pass
    elif menu == 3:
        print('\n\t프로그램을 종료합니다.')
        input('\n\t아무 키를 입력하세요.')
        break