import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
#전체 레코드 조회 readlines()와유사
#output = c.execute("SELECT * FROM Suppliers")

# 중복 레코드를 제거하는 distinct
#output = c.execute("SELECT distinct Supplier_Name from suppliers")

# WHERE 이후 여러 조건
#output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name = 'Supplier X' and Purchase_Date = '1/20/14' ")

# 부정연산자
#output = c.execute("SELECT * FROM Suppliers WHERE Part_Number <> '2341' ")

# 검색 조건 리스트
#output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name NOT IN('Supplier X', 'Supplier Y')")

# 테이블 값 정렬
#output = c.execute("select * from Suppliers order by cost")

# 전체 레코드 계산
#output = c.execute("SELECT count(*) from suppliers")

# 함수 사용 (MAX, MIN)
#output = c.execute("SELECT MIN(cost) from suppliers")
output = c.execute("SELECT MAX(cost) from suppliers")

# 열 필터링 하는 조건
# SQL문은 대소문자를 구분하지 않는다. 그렇지만 성능을 위해
# SQL문 필드, 테이블명은 일관된 대소 문자 정책을 적용해야  한다.
#output = c.execute("SELECT Supplier_Name FROM Suppliers")
#output = c.execute("SELECT Supplier_Name,Cost FROM Suppliers")
#output = c.execute("SELECT supplier_name,cost FROM suppliers")
#output = c.execute("select supplier_name,Cost FROM suppliers")
#output = c.execute("Select supplier_Name,cost FROM suppliers")

#행 필터링 조건
#output = c.execute("SELECT * FROM suppliers WHERE supplier_name='Supplier X' ")
#output = c.execute("SELECT * FROM suppliers WHERE part_number >300 ") #숙제

# 행, 열 필터링 하는 조건
#output = c.execute("SELECT supplier_name, cost FROM suppliers WHERE supplier_name ='Supplier X' ")
rows = output.fetchall()
print("Select 결과")
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)