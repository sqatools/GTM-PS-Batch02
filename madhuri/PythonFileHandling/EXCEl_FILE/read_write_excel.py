import openpyxl

def write_content_to_file(filename,sheet_name,cell_name,cell_value):
    wb = openpyxl.Workbook()
    sheet_obj = wb.active
    cell = sheet_obj[f'{cell_name}']
    cell.value = cell_value
    wb.save(filename)


#write_content_to_file("read_write_excel.xlsx", "Sheet1", "A1", "Madhuri")

def write_content_to_file_without_overwrite(filename, sheet_name, cell_name, cell_value):
    wb = openpyxl.load_workbook(filename)
    sheet_obj = wb[sheet_name]
    cell = sheet_obj[f'{cell_name}']
    cell.value = cell_value
    wb.save(filename)


write_content_to_file_without_overwrite("read_write_excel.xlsx", "Sheet2", "A2", "Modi Ji")

