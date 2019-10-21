import csv
import MySQLdb
import sys

input_file = sys.argv[1]
con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root', passwd='1111', charset='utf8')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(1,len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("""INSERT INTO my_student
    (Name,Sex,Age,Major) VALUES (
    %s, %s, %s, %s);""", data)
con.commit()