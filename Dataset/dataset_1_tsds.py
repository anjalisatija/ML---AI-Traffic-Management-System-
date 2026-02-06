import openpyxl
from openpyxl import Workbook

def read_dataset(file_path):
    with open(file_path, 'r') as file:

        lines = file.readlines()[1:]
        data = [line.strip().split(',') for line in lines]
    return data

file_path = 'C:\\Users\\Asus\\Downloads\\dataset_.txt'

data = read_dataset(file_path)

headers = ['time', 'id', 'timezone', 'pctup', 'pedestrian', 'bike', 'car', 'lorry',
           'pedestrianlft', 'bikelft', 'carlft', 'lorrylft', 'pedestrianrgt', 'bikergt',
           'carrgt', 'lorryrgt', 'carspeed00', 'carspeed10', 'carspeed20', 'carspeed30',
           'carspeed40', 'carspeed50', 'carspeed60', 'carspeed_70']

wb = Workbook()
ws = wb.active

ws.append(headers)


for row in data:
    ws.append(row)

# Changinf name of excel file !!

wb.save('C:\\Users\\Asus\\Downloads\\traffic_data_1.xlsx')

print("Data has been exported to traffic_data_no_pandas.xlsx")
