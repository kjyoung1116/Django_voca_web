from re import S
import openpyxl

wb = openpyxl.load_workbook('voca.xlsx') 
ws = wb['Sheet1']

print(ws["h2"].value.replace('1.','/'))

