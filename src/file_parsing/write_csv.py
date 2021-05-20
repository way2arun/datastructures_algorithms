import random
import uuid
import time
from xlsxwriter import Workbook
import csv
"""
outfile = 'data.csv'
outsize = 1024 * 1024 #1024 * 1024 * 1024 # 1GB
start_time = time.time()
with open(outfile, 'ab') as csvfile:
    size = 0
    while size < outsize:
        txt = '%s,%.6f,%.6f,%i\n' % (uuid.uuid4(), random.random()*50, random.random()*50, random.randrange(1000))
        size += len(txt)
        csvfile.write(txt.encode())
print("file write took %s seconds" % (time.time() - start_time))

import csvstart_time = time.time()
with open("fruits.csv", "w") as csv_file:
    size = 0
    while size < outsize:
        txt = '%s,%.6f,%.6f,%i\n' % (uuid.uuid4(), random.random() * 50, random.random() * 50, random.randrange(1000))
        size += len(txt)
        csv_writer = csv.DictWriter(csv_file, txt.encode())
        csv_writer.writeheader()

print("file write took %s seconds" % (time.time() - start_time))
"""
"""
start_time = time.time()
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

workbook = Workbook("worksheet.xlsx", {'constant_memory': True})
worksheet = workbook.add_worksheet("sheet1")
# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
print("file write took %s seconds" % (time.time() - start_time))

"""

"""
def write_data_xlsxwriter(self, count, export_sheet_name ):
    workbook = Workbook(self.export_file,)
    worksheet = workbook.add_worksheet(export_sheet_name)

    for index in range(1, count+1, 10000):
        data = self.get_sql_data(start=index, end=index+10000)

        row = 0
        col = 0

        for row_data in data:
            col = 0
            for data_set in row_data:
                worksheet.write(row, col, data_set)
                col += 1

            row += 1
    workbook.close()
"""
start_time = time.time()
data_iterator = ["Arun", "XYZ", "TinTin"]
for index, row in enumerate(data_iterator):
    print(index, row)

with open("fast_csv.csv", 'wb') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, extrasaction='ignore', fieldnames=fieldnames)
    #writer.writeheader()
    #writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    #writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    for index, row in enumerate(data_iterator):
        writer.writerow(row)
print("file write took %s seconds" % (time.time() - start_time))




