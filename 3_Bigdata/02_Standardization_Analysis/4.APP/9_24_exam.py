import csv
import MySQLdb
import sys
import mysql.connector

input_file = sys.argv[1] #item_numbers_to_find.csv
path_to_folder = sys.argv[2] #historical_files
output_file = sys.argv[3] #output_files/1output.csv
con = MySQLdb.connect(host='localhost', port=3306, db='data_exam', user='root', passwd='1111', charset='utf8')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("""INSERT INTO data_exam
    (Item_Numbers, Description, Suppliers, Cost, Date) VALUES (
    %s, %s, %s, %s, %s);""", data)
con.commit()