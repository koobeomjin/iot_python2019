import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a csv input file
input_file = sys.argv[1] # output_files/suppliers_2012.csv
con = MySQLdb.connect(host='localhost', port=3306,db='data_exam',user='open_source',passwd='1111')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index == 0:
            try:
                data.append(int(row[column_index]))
            except:
                data.append(0)
        elif column_index > 0 and column_index < 3:
            data.append(row[column_index])
        elif column_index == 3:
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        else:
            a_data = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%Y'))
            a_data = a_data.strftime('%y-%m-%d')
            data.append(a_data)
    print(data)
    c.execute("""INSERT INTO data_exam VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

c.execute("SELECT * FROM data_exam")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)