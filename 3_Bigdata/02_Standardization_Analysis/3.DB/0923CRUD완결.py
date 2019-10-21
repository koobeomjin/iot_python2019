import csv
import MySQLdb
import sys
import sqlite3
from datetime import datetime, date

#create table if not exists Student_Info
#  ( Student_ID int not null auto_increment primary key,
#   Name VARCHAR(20),
#   Sex VARCHAR(20),
#   Age INT,
#   Major VARCHAR(20));

con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root', passwd='1111', charset='utf8')
c = con.cursor()

start = """<메인메뉴>
1. 생성(Insert)
2. 조회(Select)
3. 변경(Update)
4. 삭제(Delete)
5. 종료"""

def insertdata(insert):
    insert = insert.split()
    insert[2] = int(insert[2])
    c.execute("""INSERT INTO Basic_Student_Info
    (Name,Sex,Age,Major) VALUES (%s, %s, %s, %s);""", insert)
    con.commit()
    print('데이터가 저장되었습니다.')
    print('')


def select():
    sub1 = """<2. 데이터 조회>
1. 전체 조회
2. 이름 조회
3. 아이디 조회
4. 나이 조회
5. 전공 조회
6. 이전 메뉴"""
    while 1:
        print(sub1)
        sub2 = input('메뉴를 입력하세요: ')
        if sub2 == '1':
            c.execute("SELECT * FROM Basic_Student_Info")
            rows = c.fetchall()
            for row in rows:
                row_list_output = []
                for column_index in range(len(row)):
                    row_list_output.append(str(row[column_index]))
                print(row_list_output)
        elif sub2 == '2':
            sub3 = input('이름을 입력하세요: ')
            sub4 = c.execute(f"SELECT * FROM Basic_Student_Info WHERE name='{sub3}' ")
            rows = c.fetchall()
            for row in rows:
                row_list_output = []
                for column_index in range(len(row)):
                    row_list_output.append(str(row[column_index]))
                print(row_list_output)
            if sub4 == False:
                print('일치하는 데이터가 없습니다.')
                print('')
        elif sub2 == '3':
            sub3 = input('아이디를 입력하세요: ')
            sub4 = c.execute(f"SELECT * FROM Basic_Student_Info WHERE Student_ID='{int(sub3)}' ")
            rows = c.fetchall()
            for row in rows:
                row_list_output = []
                for column_index in range(len(row)):
                    row_list_output.append(str(row[column_index]))
                print(row_list_output)
            if sub4 == False:
                print('일치하는 데이터가 없습니다.')
                print('')
        elif sub2 == '4':
            print('나이를 입력하세요.(무조건 양식에 맞춰서입력)     ex1) 15~15   ex2) 10~20')
            sub3 = input('나이를 입력하세요: ')
            sub3 = sub3.split('~')
            sub3[0] = int(sub3[0])
            sub3[1] = int(sub3[1])
            sub4 = c.execute(f"SELECT * FROM Basic_Student_Info WHERE age >= {sub3[0]} and age <= {sub3[1]} ")
            rows = c.fetchall()
            for row in rows:
                row_list_output = []
                for column_index in range(len(row)):
                    row_list_output.append(str(row[column_index]))
                print(row_list_output)
            if sub4 == False:
                print('일치하는 데이터가 없습니다.')
                print('')
        elif sub2 == '5':
            sub3 = input('전공을 입력하세요: ')
            sub4 = c.execute(f"SELECT * FROM Basic_Student_Info WHERE Major='{sub3}' ")
            rows = c.fetchall()
            for row in rows:
                row_list_output = []
                for column_index in range(len(row)):
                    row_list_output.append(str(row[column_index]))
                print(row_list_output)
            if sub4 == False:
                print('일치하는 데이터가 없습니다.')
                print('')
        else:
            return


def Update():
    while 1:
        sub3 = int(input('아이디를 입력하세요(이전메뉴로 가시려면 0을 입력하여주세요): '))
        if sub3 == 0:
            return
        sub4 = c.execute(f"SELECT * FROM Basic_Student_Info WHERE Student_ID='{sub3}' ")
        rows = c.fetchall()
        for row in rows:
            row_list_output = []
            for column_index in range(len(row)):
                row_list_output.append(str(row[column_index]))
            print(row_list_output)
        if sub4 == False:
            print('일치하는 데이터가 없습니다.')
            continue
        print('이름, 성별, 나이, 전공 순으로 새로운 데이터를 입력 하세요. 예) 홍길동 남 45 행정학')
        aa = input('데이터 입력: ')
        aa = aa.split()
        aa[2] = int(aa[2])
        aa = aa+[sub3]
        print(aa)
        c.execute(f"""UPDATE Student_info SET Name=%s, Sex=%s, Age=%s, Major=%s WHERE Student_Id=%s""", aa)
        con.commit()
        print('변경되었습니다.')
        print('')




def Delete():
    while 1:
        ddd = int(input('아이디를 입력하세요(이전메뉴로 가시려면 0을 입력하여주세요): '))
        if ddd == 0:
            return
        sub4 = c.execute(f"SELECT * FROM Basic_Student_Info WHERE Student_ID='{ddd}' ")
        if sub4 == False:
            print('일치하는 데이터가 없습니다.')
            continue
        delete_table = f"""
        delete
        from Basic_Student_Info
        where Student_ID='{ddd}'
        """

        check = input('삭제하시겠습니까? (Y/N): ' )
        if check == 'Y' or check ==  'y':
            c.execute(delete_table)
            con.commit()
            print('삭제되었습니다.')
        else:
            continue





while 1:
    print(start)
    hi = input("메뉴를 선택하여주세요: ")
    if hi == '1':
        print('1. 데이터 생성')
        print('이름, 성별, 나이, 전공 순으로 데이터를 입력 하세요. 예) 홍길동 남 45 행정학')
        insert = input('데이터 입력: ')
        insertdata(insert)
    elif hi == '2':
        select()
    elif hi == '3':
        Update()
    elif hi == '4':
        Delete()
    else:
        exit()
