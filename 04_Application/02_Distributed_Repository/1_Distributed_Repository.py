import csv

def get_request_url():
    pass

def getTourPointVisitor():
    pass

def getTourPointData():
    filewriter.writerow(simulation_data)
    return

output_file = '시뮬레이션_서울특별시_관광지별_방문객.csv'

csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
header_list = ['addrCd','gungu','sido','resNm','rnum','csForCnt','csNatCnt']
simulation_data = ['1111','종로구','서울특별시','창덕궁','1','14137','43677']
filewriter.writerow(header_list)

getTourPointData()
csv_out_file.close()