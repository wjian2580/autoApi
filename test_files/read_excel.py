#coding = utf-8

from configparser import ConfigParser
import xlrd
import requests


def read_excel():
	cf = ConfigParser()
	data = xlrd.open_workbook('test.xlsx')
	table = data.sheets()[0]
	for i in range(table.nrows-1):
		case = table.row_values(i+1)
		case_name = case[1]
		case_url = case[2]
		case_method = case[3]
		case_data = case[4]


		cf.add_section(case_name)
		cf.set(case_name, 'case_url',case_url)
		cf.set(case_name, 'case_method',case_method)
		cf.set(case_name, 'case_data',case_data)
	cf.write(open('api.ini','w',encoding='utf-8'))

if __name__ == '__main__':
	read_excel()




