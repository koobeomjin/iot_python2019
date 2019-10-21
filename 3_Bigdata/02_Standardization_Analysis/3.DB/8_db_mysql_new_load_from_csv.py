import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a csv input file
input_file = sys.argv[1] # suppliers_2012.csv
con = MySQLdb.connect(host='localhost', port=3306,db='my_suppliers',user='open_source',passwd='1111')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        # print(column_index)














        if column_index == 3:
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        elif column_index < 3:
            data.append()
        else:
            a_data = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
            a_data = a_data.strftime('%y-%m-%d')
            data.append(a_data)
    print(data)
    c.execute("""INSERT INTO data_exam VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)