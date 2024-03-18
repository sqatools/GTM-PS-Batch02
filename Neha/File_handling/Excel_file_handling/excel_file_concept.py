import openpyxl


def read_excel_data(filename, row_num, col_num, sheet_name):
    wb = openpyxl.load_workbook(filename)
    excel_sheet = wb[f'{sheet_name}']
    #print(excel_sheet)
    cell_obj = excel_sheet.cell(row=row_num, column=col_num)
    print(cell_obj.value)