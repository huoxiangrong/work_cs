import openpyxl
import filecmp
from openpyxl import load_workbook

def check(file0_name, file1_name):
    ret = filecmp.cmp(file0_name, file1_name, shallow=True)
    print("compare bootloader file, result: %s\n" % ret)


def compare_bl():
    file_path = r'E:\work\doc\bin\\'
    chip_name = 'chip5_bl.bin'
    bl_name = 'onchip_bl.bin'

    file0_name = file_path + bl_name
    file1_name = file_path + chip_name

    check(file0_name, file1_name)


def excel_proc(dat):
    filename = r"C:\Users\work\Desktop\data\tsensor_data.xlsx"
    wb = load_workbook(filename=filename)
    sheet = wb['Sheet1']
    for i in dat:
        find_dat(sheet, i)


def find_dat(sheet, dat):
    for row in sheet.rows:
        if row[0].value == dat:
            for i in row:
                print(i)
                print(i.value)



if __name__ == '__main__':
    dat = ['6_91']
    excel_proc(dat)
