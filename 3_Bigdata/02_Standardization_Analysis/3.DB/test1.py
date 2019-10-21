import csv
import MySQLdb
import sqlite3
import sys

input_file = sys.argv[1] #supplier_data.csv

con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root', passwd='1111', charset='utf8')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS my_student
                (Student_ID int not null auto_increment primary key,
                Name VARCHAR(20),
                Sex VARCHAR(20),
                Age int,
                Major VARCHAR(20)
                );"""
c.execute(create_table)
con.commit()

#Read the CSV file
#Insert the data into the Supplier table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None) #header 건너뛰고 data만 접근 하기 위하여
for row in file_reader:
    data = []
    for column_index in range(1, len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Students Info (?, ?, ?, ?);", data)
con.commit()

# Query the Suppliers table
output = c.execute("SELECT * FROM Student_Info")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)